// 이 repo의 '문제 풀이' 커밋만 집계해 잔디 히트맵 SVG를 생성한다.
// - SOLVED_DIR({프로그래머스}) 하위에 파일이 '추가(A)'된 커밋만 카운트한다.
//   (README·SVG 갱신, 봇 자동 커밋, 문서 수정 등은 잔디에 반영되지 않는다 →
//    문제를 실제로 풀지 않으면 스트릭이 유지되지 않도록.)
// 실행: node .github/scripts/streak-grass.mjs
import { execSync } from 'node:child_process';
import { writeFileSync, mkdirSync } from 'node:fs';

const TZ = 'Asia/Seoul';
const SOLVED_DIR = process.env.SOLVED_DIR || '프로그래머스'; // BaekjoonHub 풀이 폴더

// ---- 풀이 커밋 날짜 → 날짜별 커밋수 집계 (KST 기준) ----
function collectCounts() {
  // --diff-filter=A + 경로 지정: SOLVED_DIR 안에 파일을 새로 추가한 커밋만.
  const out = execSync(
    `git log --no-merges --diff-filter=A --pretty=%ad --date=format-local:%Y-%m-%d -- "${SOLVED_DIR}"`,
    { encoding: 'utf8', env: { ...process.env, TZ } }
  ).trim();
  const counts = {};
  if (out) for (const line of out.split('\n')) {
    const k = line.trim();
    if (k) counts[k] = (counts[k] || 0) + 1;
  }
  return counts;
}

function today() {
  const s = new Date().toLocaleDateString('en-CA', { timeZone: TZ }); // YYYY-MM-DD
  return s;
}

function computeStats(counts, end) {
  const total = Object.values(counts).reduce((a, b) => a + b, 0);
  // 현재 연속: 오늘(또는 어제)부터 거꾸로
  const day = (d) => d.toISOString().slice(0, 10);
  const e = new Date(end + 'T00:00:00Z');
  let cur = 0;
  // 오늘 커밋 없으면 어제까지의 연속을 살아있는 걸로 인정
  let cursor = new Date(e);
  if (!counts[day(cursor)]) cursor.setUTCDate(cursor.getUTCDate() - 1);
  while (counts[day(cursor)]) { cur++; cursor.setUTCDate(cursor.getUTCDate() - 1); }
  // 최장 연속 & 시작일
  const keys = Object.keys(counts).sort();
  let longest = 0, run = 0, prev = null, curStart = null;
  for (const k of keys) {
    const d = new Date(k + 'T00:00:00Z');
    if (prev && (d - prev) === 86400000) run++; else run = 1;
    if (run > longest) longest = run;
    prev = d;
  }
  const firstDay = keys[0] || end;
  // 현재 연속 시작일
  if (cur > 0) { const c = new Date(e); if (!counts[day(c)]) c.setUTCDate(c.getUTCDate()-1); c.setUTCDate(c.getUTCDate()-(cur-1)); curStart = day(c); }
  return { total, cur, longest, firstDay, curStart };
}

// ---- 히트맵 SVG ----
function heatmap(counts, end, theme) {
  const t = theme === 'dark'
    ? { card: '#22272e', text: '#adbac7', sub: '#768390', border: '#444c56',
        lv: ['#2d333b', '#0e4429', '#006d32', '#26a641', '#39d353'] }
    : { card: '#ffffff', text: '#24292f', sub: '#57606a', border: '#d0d7de',
        lv: ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39'] };

  const cell = 13, gap = 5, step = cell + gap, gridLeft = 46, gridTop = 78;
  const padX = 22;
  const endDate = new Date(end + 'T00:00:00Z');
  const firstReal = new Date(endDate); firstReal.setUTCDate(firstReal.getUTCDate() - 363);
  // 일요일 시작으로 패딩
  const start = new Date(firstReal);
  start.setUTCDate(start.getUTCDate() - start.getUTCDay());

  const level = (c) => c === 0 ? 0 : c === 1 ? 1 : c === 2 ? 2 : c <= 4 ? 3 : 4;
  const MON = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const key = (d) => d.toISOString().slice(0, 10);

  let rects = '', weeks = 0, idx = 0, lastMonth = -1, monthText = '';
  for (let d = new Date(start); d <= endDate; d.setUTCDate(d.getUTCDate() + 1), idx++) {
    const wk = Math.floor(idx / 7), dow = idx % 7;
    weeks = Math.max(weeks, wk + 1);
    const inRange = d >= firstReal;
    const c = counts[key(d)] ?? 0;
    const x = gridLeft + wk * step, y = gridTop + dow * step;
    rects += `<rect x="${x}" y="${y}" width="${cell}" height="${cell}" rx="3" fill="${inRange ? t.lv[level(c)] : 'transparent'}"/>`;
    if (dow === 0 && inRange && d.getUTCMonth() !== lastMonth) {
      lastMonth = d.getUTCMonth();
      monthText += `<text x="${x}" y="${gridTop - 14}" fill="${t.sub}" font-size="11">${MON[lastMonth]}</text>`;
    }
  }
  const dowLabels = [['Mon',1],['Wed',3],['Fri',5]].map(([lab,i]) =>
    `<text x="${gridLeft-10}" y="${gridTop+i*step+cell-2}" fill="${t.sub}" font-size="10" text-anchor="end">${lab}</text>`).join('');

  const W = gridLeft + weeks * step - gap + padX, H = gridTop + 7 * step - gap + 52;
  const st = computeStats(counts, end);
  const legX = W - 208, legY = H - 26;
  let legend = `<text x="${legX-6}" y="${legY+10}" fill="${t.sub}" font-size="11" text-anchor="end">Less</text>`;
  t.lv.forEach((c, i) => legend += `<rect x="${legX+i*step}" y="${legY}" width="${cell}" height="${cell}" rx="3" fill="${c}"/>`);
  legend += `<text x="${legX+5*step+4}" y="${legY+10}" fill="${t.sub}" font-size="11">More</text>`;

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" font-family="'Segoe UI',Ubuntu,sans-serif">
  <rect x="0.5" y="0.5" width="${W-1}" height="${H-1}" rx="12" fill="${t.card}" stroke="${t.border}"/>
  <text x="${padX}" y="42" fill="${t.text}" font-size="16" font-weight="600">🌱 programmers-daily</text>
  <text x="${W-padX}" y="42" fill="${t.text}" font-size="20" font-weight="700" text-anchor="end">🔥 ${st.cur}<tspan font-size="12" font-weight="400" fill="${t.sub}"> 일 연속</tspan></text>
  ${monthText}${dowLabels}${rects}${legend}
</svg>`;
}

// ---- main ----
const counts = collectCounts();
const end = today();
mkdirSync('assets', { recursive: true });
writeFileSync('assets/heatmap-dark.svg', heatmap(counts, end, 'dark'));
writeFileSync('assets/heatmap-light.svg', heatmap(counts, end, 'light'));
const st = computeStats(counts, end);
console.log(`grass updated: total=${st.total}, current=${st.cur}, longest=${st.longest}`);
