// 프로그래머스 공개 API에서 '오늘의 문제'를 뽑아 README의
// <!-- TODAY:START --> ~ <!-- TODAY:END --> 구간을 갱신한다.
//
// - 지정한 레벨(기본 2,3,4)에서 각 1문제씩 뽑아 순서를 랜덤하게 섞는다.
//   (표시에는 난이도를 노출하지 않는다 — 풀기 전 스포 방지)
// - 이미 푼 문제({SOLVED_DIR}/{레벨}/{id}. {제목} 폴더)는 후보에서 제외
// - KST 날짜로 시드를 고정 → 같은 날은 몇 번 실행해도 같은 결과 (churn 방지)
// - 리롤: REROLL=1 이면 그날의 salt를 +1 해 새로 뽑고, 그 값을 파일로 저장해
//         이후 (커밋 push 등으로) 재실행돼도 리롤 결과가 유지된다.
//
// 설정(환경변수, 전부 선택):
//   PICK_LEVELS   기본 "2,3,4"    (각 레벨에서 1문제씩)
//   PICK_LANG     기본 "" (전체)  해당 언어로 제출 가능한 문제만 (예: python3, cpp)
//   SOLVED_DIR    기본 "프로그래머스" (BaekjoonHub 풀이 폴더)
//   README_PATH   기본 "README.md"
//   REROLL        "1"/"true" 면 다시 뽑기
//
// 실행: node .github/scripts/pick-problem.mjs
import { readdirSync, statSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const TZ = 'Asia/Seoul';
const API = 'https://school.programmers.co.kr/api/v2/school/challenges/';
const README = process.env.README_PATH || 'README.md';
const SOLVED_DIR = process.env.SOLVED_DIR || '프로그래머스';
const SALT_FILE = '.github/.today-salt';
const LEVELS = (process.env.PICK_LEVELS || '2,3,4')
  .split(',').map((s) => Number(s.trim())).filter((n) => Number.isFinite(n));
// 제출 언어 필터: 비우면 전체, 지정하면 그 언어로 풀 수 있는 문제만 (프로그래머스 API 지원)
const VALID_LANGS = ['c', 'cpp', 'csharp', 'go', 'java', 'javascript',
  'kotlin', 'python3', 'ruby', 'scala', 'swift', 'mysql', 'oracle'];
const LANG = (process.env.PICK_LANG || '').trim().toLowerCase();
if (LANG && !VALID_LANGS.includes(LANG)) {
  console.error(`PICK_LANG="${LANG}" 은 지원하지 않는 값입니다. 가능: ${VALID_LANGS.join(', ')}`);
  process.exit(1);
}

// ---- 날짜 시드 PRNG (mulberry32) ----
function today() {
  return new Date().toLocaleDateString('en-CA', { timeZone: TZ }); // YYYY-MM-DD
}
function hashSeed(str) {
  let h = 2166136261 >>> 0;
  for (const ch of str) { h ^= ch.charCodeAt(0); h = Math.imul(h, 16777619); }
  return h >>> 0;
}
function mulberry32(a) {
  return function () {
    a |= 0; a = (a + 0x6D2B79F5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ---- 리롤 salt (오늘 날짜 기준으로만 유효) ----
function loadSalt(date) {
  try {
    const [d, n] = readFileSync(SALT_FILE, 'utf8').trim().split(':');
    if (d === date) return parseInt(n, 10) || 0;
  } catch { /* 파일 없음 */ }
  return 0;
}
function resolveSalt(date) {
  let salt = loadSalt(date);
  const reroll = String(process.env.REROLL || '').toLowerCase();
  if (['1', 'true', 'yes', 'on'].includes(reroll)) salt += 1;
  writeFileSync(SALT_FILE, `${date}:${salt}\n`);
  return salt;
}

// ---- 이미 푼 문제 id 수집 ----
function solvedIds() {
  const set = new Set();
  if (!existsSync(SOLVED_DIR)) return set;
  for (const lvl of readdirSync(SOLVED_DIR)) {
    const dir = join(SOLVED_DIR, lvl);
    if (!statSync(dir).isDirectory()) continue;
    for (const name of readdirSync(dir)) {
      const m = name.match(/^(\d+)\./); // "159993. 미로 탈출" → 159993
      if (m) set.add(Number(m[1]));
    }
  }
  return set;
}

// ---- API에서 특정 레벨의 전체 문제 목록 (페이지네이션) ----
async function fetchLevel(level) {
  const all = [];
  let page = 1, totalPages = 1;
  do {
    const langQ = LANG ? `&languages%5B%5D=${LANG}` : '';
    const url = `${API}?perPage=100&levels%5B%5D=${level}&order=recent&search=${langQ}&page=${page}`;
    const res = await fetch(url, {
      headers: { 'User-Agent': 'programmers-daily-bot', 'Accept': 'application/json' },
    });
    if (!res.ok) throw new Error(`API ${res.status} (level ${level}, page ${page})`);
    const data = await res.json();
    for (const p of data.result ?? []) all.push({ ...p, level });
    totalPages = data.totalPages ?? 1;
    page++;
  } while (page <= totalPages);
  return all;
}

function renderBlock(date, picks) {
  const lines = picks.map((p, i) => {
    const url = `https://school.programmers.co.kr/learn/courses/30/lessons/${p.id}`;
    return `${i + 1}. [${p.title}](${url})`;
  });
  return (
    `**오늘의 문제 · ${date}**\n\n` +
    lines.join('\n') +
    `\n\n<sub>매일 자정(KST) 자동 갱신 · 다시 뽑기: Actions → 해당 워크플로 → Run workflow(reroll 체크)</sub>`
  );
}

async function main() {
  const date = today();
  const salt = resolveSalt(date);
  const prng = mulberry32(hashSeed(`${date}:${salt}`));
  const solved = solvedIds();

  // 레벨별로 안 푼 문제 중 1개씩
  const lists = await Promise.all(LEVELS.map(fetchLevel));
  const picks = [];
  lists.forEach((list) => {
    const cands = list.filter((p) => !solved.has(p.id));
    if (cands.length) picks.push(cands[Math.floor(prng() * cands.length)]);
  });
  if (!picks.length) throw new Error(`안 푼 문제를 찾지 못했습니다 (레벨 ${LEVELS.join(',')}).`);

  // 표시 순서 셔플 (난이도 순서로 유추 못 하게) — Fisher-Yates
  for (let i = picks.length - 1; i > 0; i--) {
    const j = Math.floor(prng() * (i + 1));
    [picks[i], picks[j]] = [picks[j], picks[i]];
  }

  const md = readFileSync(README, 'utf8');
  const re = /(<!-- TODAY:START -->)[\s\S]*?(<!-- TODAY:END -->)/;
  if (!re.test(md)) throw new Error('README에 <!-- TODAY:START --> / <!-- TODAY:END --> 마커가 없습니다.');
  writeFileSync(README, md.replace(re, `$1\n${renderBlock(date, picks)}\n$2`));

  console.log(`오늘의 문제 ${picks.length}개 (salt=${salt}):`);
  for (const p of picks) console.log(`  [Lv.${p.level}] ${p.title}`);
}

main().catch((e) => { console.error(e.message); process.exit(1); });
