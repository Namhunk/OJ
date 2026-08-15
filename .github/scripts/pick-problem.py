#!/usr/bin/env python3
"""
프로그래머스 내부 API에서 '오늘의 문제'를 뽑아 README의
<!-- TODAY:START --> ~ <!-- TODAY:END --> 구간을 갱신한다.

- 지정한 레벨(기본 2,3,4)에서 각 1문제씩 뽑아 순서를 랜덤하게 섞는다.
  (표시에는 난이도를 노출하지 않는다 — 풀기 전 스포 방지)
- 이미 푼 문제({SOLVED_DIR}/{레벨}/{id}. {제목} 폴더)는 후보에서 제외
- KST 날짜로 시드를 고정 → 같은 날은 몇 번 실행해도 같은 결과 (churn 방지)
- 리롤: REROLL=1 이면 그날의 salt를 +1 해 새로 뽑고, 그 값을 파일로 저장해
        이후 (커밋 push 등으로) 재실행돼도 리롤 결과가 유지된다.

설정(환경변수, 전부 선택):
  PICK_LEVELS   기본 "2,3,4"    (각 레벨에서 1문제씩)
  PICK_LANG     기본 "" (전체)  해당 언어로 제출 가능한 문제만 (예: python3, cpp)
  SOLVED_DIR    기본 "프로그래머스" (BaekjoonHub 풀이 폴더)
  README_PATH   기본 "README.md"
  REROLL        "1"/"true" 면 다시 뽑기

실행: python .github/scripts/pick_problem.py

표준 라이브러리만 사용 (외부 의존성 없음 — CI에 pip install 불필요).
"""
from __future__ import annotations

import json
import os
import random
import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
API = "https://school.programmers.co.kr/api/v2/school/challenges/"
README = Path(os.environ.get("README_PATH", "README.md"))
SOLVED_DIR = Path(os.environ.get("SOLVED_DIR", "프로그래머스"))
SALT_FILE = Path(".github/.today-salt")

VALID_LANGS = [
    "c", "cpp", "csharp", "go", "java", "javascript",
    "kotlin", "python3", "ruby", "scala", "swift", "mysql", "oracle",
]

LEVELS = [
    int(s.strip())
    for s in os.environ.get("PICK_LEVELS", "2,3,4").split(",")
    if s.strip().lstrip("-").isdigit()
]

LANG = os.environ.get("PICK_LANG", "").strip().lower()
if LANG and LANG not in VALID_LANGS:
    print(f'PICK_LANG="{LANG}" 은 지원하지 않는 값입니다. 가능: {", ".join(VALID_LANGS)}', file=sys.stderr)
    sys.exit(1)


# ---- 날짜 시드 ----
def today() -> str:
    return datetime.now(KST).strftime("%Y-%m-%d")


def hash_seed(s: str) -> int:
    # JS 버전(FNV-1a 32bit)과 동일한 해시 → 필요하면 결과를 맞출 수 있음.
    # (Python random과 결과가 1:1로 같을 필요는 없어서 그대로 seed로만 사용)
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return h


# ---- 리롤 salt (오늘 날짜 기준으로만 유효) ----
def load_salt(date: str) -> int:
    try:
        d, n = SALT_FILE.read_text(encoding="utf-8").strip().split(":")
        if d == date:
            return int(n)
    except (FileNotFoundError, ValueError):
        pass
    return 0


def resolve_salt(date: str) -> int:
    salt = load_salt(date)
    if os.environ.get("REROLL", "").strip().lower() in ("1", "true", "yes", "on"):
        salt += 1
    SALT_FILE.parent.mkdir(parents=True, exist_ok=True)
    SALT_FILE.write_text(f"{date}:{salt}\n", encoding="utf-8")
    return salt


# ---- 이미 푼 문제 id 수집 ----
def solved_ids() -> set[int]:
    ids: set[int] = set()
    if not SOLVED_DIR.exists():
        return ids
    for lvl_dir in SOLVED_DIR.iterdir():
        if not lvl_dir.is_dir():
            continue
        for entry in lvl_dir.iterdir():
            m = re.match(r"^(\d+)\.", entry.name)  # "159993. 미로 탈출" → 159993
            if m:
                ids.add(int(m.group(1)))
    return ids


# ---- API에서 특정 레벨의 전체 문제 목록 (페이지네이션) ----
def fetch_level(level: int) -> list[dict]:
    all_problems: list[dict] = []
    page = 1
    total_pages = 1
    while page <= total_pages:
        lang_q = f"&languages%5B%5D={LANG}" if LANG else ""
        url = f"{API}?perPage=100&levels%5B%5D={level}&order=recent&search={lang_q}&page={page}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "programmers-daily-bot", "Accept": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=15) as res:
                data = json.loads(res.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"API {e.code} (level {level}, page {page})") from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"API 요청 실패 (level {level}, page {page}): {e.reason}") from e

        for p in data.get("result") or []:
            item = dict(p)
            item["level"] = level
            all_problems.append(item)
        total_pages = data.get("totalPages") or 1
        page += 1
    return all_problems


def render_block(date: str, picks: list[dict]) -> str:
    lines = []
    for i, p in enumerate(picks, start=1):
        url = f"https://school.programmers.co.kr/learn/courses/30/lessons/{p['id']}"
        lines.append(f"{i}. [{p['title']}]({url})")
    body = "\n".join(lines)
    return (
        f"**오늘의 문제 · {date}**\n\n"
        f"{body}\n\n"
        f"<sub>매일 자정(KST) 자동 갱신 · 다시 뽑기: Actions → 해당 워크플로 → "
        f"Run workflow(reroll 체크)</sub>"
    )


def main() -> None:
    date = today()
    salt = resolve_salt(date)
    rng = random.Random(hash_seed(f"{date}:{salt}"))
    solved = solved_ids()

    # 레벨별로 안 푼 문제 중 1개씩
    picks: list[dict] = []
    for level in LEVELS:
        candidates = [p for p in fetch_level(level) if p["id"] not in solved]
        if candidates:
            picks.append(rng.choice(candidates))

    if not picks:
        raise RuntimeError(f"안 푼 문제를 찾지 못했습니다 (레벨 {','.join(map(str, LEVELS))}).")

    # 표시 순서 셔플 (난이도 순서로 유추 못 하게)
    rng.shuffle(picks)

    md = README.read_text(encoding="utf-8")
    pattern = re.compile(r"(<!-- TODAY:START -->)[\s\S]*?(<!-- TODAY:END -->)")
    if not pattern.search(md):
        raise RuntimeError("README에 <!-- TODAY:START --> / <!-- TODAY:END --> 마커가 없습니다.")

    new_md = pattern.sub(lambda m: f"{m.group(1)}\n{render_block(date, picks)}\n{m.group(2)}", md)
    README.write_text(new_md, encoding="utf-8")

    print(f"오늘의 문제 {len(picks)}개 (salt={salt}):")
    for p in picks:
        print(f"  [Lv.{p['level']}] {p['title']}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001
        print(str(e), file=sys.stderr)
        sys.exit(1)
