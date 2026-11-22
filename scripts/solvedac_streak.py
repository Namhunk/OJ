"""solved.ac 스트릭(잔디) SVG 생성기 — solved.ac 프로필의 스트릭 카드 모양을 재현.

환경 변수
  SOLVEDAC_HANDLE         백준 아이디 (필수)
  SOLVEDAC_CLIENT_ID      Backstage 앱 client ID (필수)
  SOLVEDAC_CLIENT_SECRET  Backstage 앱 client secret (필수)
  OUTPUT_PATH             저장할 SVG 경로 (기본값: solvedac-streak.svg)
  STREAK_MODE             count(푼 문제 수, 기본값) 또는 level(난이도)

표준 라이브러리만 사용하므로 pip 설치가 필요 없습니다.
"""

import json
import math
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, timedelta, timezone

API = "https://solved.ac/api/v4"
KST = timezone(timedelta(hours=9))

# solved.ac 다크 테마 색 (스크린샷에서 추출)
PAGE_BG = "#09090b"
CARD_BG = "#181a1c"
HEADER_BG = "#191d1e"
EMPTY = "#2a2c2f"
TEXT = "#e5e7eb"
SUB = "#a9b5b6"
GREEN = "#4ade80"
VACATION = "#724a29"
COUNT_COLORS = ["#ffd459", "#ffaa69", "#ff7c79", "#ff5f84"]  # 적음 → 많음

# 난이도 모드: 그날 푼 가장 어려운 문제의 티어 색
TIER_GROUP_COLORS = ["#ad5600", "#435f7a", "#ec9a00", "#27e2a4", "#00b4fc", "#ff0062"]


def api_get(path, params=None):
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={
        "x-client-id": os.environ["SOLVEDAC_CLIENT_ID"],
        "x-client-secret": os.environ["SOLVEDAC_CLIENT_SECRET"],
        "Accept": "application/json",
        "User-Agent": "solvedac-streak-card",
    })
    try:
        with urllib.request.urlopen(req, timeout=20) as res:
            return json.load(res)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:500]
        sys.exit(f"API 오류 {e.code} ({path}): {body}")


def cell_color(info, mode, max_count):
    count = info.get("solvedCount", 0)
    if count <= 0:
        return EMPTY
    if mode == "level":
        level = info.get("maxSolvedLevel", 0)
        if level <= 0:
            return EMPTY
        return TIER_GROUP_COLORS[min((level - 1) // 5, 5)]
    # 푼 문제 수: 기간 내 최대값 기준 4단계
    idx = math.ceil(4 * count / max(max_count, 1)) - 1
    return COUNT_COLORS[max(0, min(idx, 3))]


def build_svg(profile, activity, today, mode="count"):
    days = activity.get("days", [])
    by_day = {d["day"]: d for d in days}
    max_count = activity.get("maxSolvedCount") or max((d.get("solvedCount", 0) for d in days), default=1)

    vacation_from = None
    vac = profile.get("streakVacation")
    if vac and vac.get("fromDay"):
        vacation_from = date.fromisoformat(vac["fromDay"][:10])

    def on_vacation(d):
        info = by_day.get(d.isoformat(), {})
        if info.get("solvedCount", 0) > 0:
            return False
        return (vacation_from is not None and d >= vacation_from) or bool(info.get("freezeUsed"))

    cell, gap = 12, 4
    step = cell + gap
    weeks = 53
    pad = 24
    width = pad * 2 + 26 + weeks * step
    header_h = 88
    grid_top = header_h + 16 + 40          # 두 번째 카드 안 월 라벨 아래
    grid_left = pad + 26
    grid_h = 7 * step
    card2_y = header_h + 16
    card2_h = 40 + grid_h + 56
    height = card2_y + card2_h

    end = today + timedelta(days=(5 - today.weekday()) % 7)   # 이번 주 토요일
    start = end - timedelta(days=weeks * 7 - 1)                # 53주 전 일요일

    parts = []
    month_seen = None
    for w in range(weeks):
        ws = start + timedelta(days=w * 7)
        x = grid_left + w * step
        if ws.month != month_seen and ws.day <= 7:
            parts.append(f'<text x="{x}" y="{grid_top - 10}" class="m">{ws.month}월</text>')
            month_seen = ws.month

        # 휴가 구간은 주 단위로 세로로 긴 테두리 막대로 묶어서 그림
        run_start = None
        for dow in range(8):
            d = ws + timedelta(days=dow)
            vac_here = dow < 7 and d <= today and on_vacation(d)
            if vac_here and run_start is None:
                run_start = dow
            if not vac_here and run_start is not None:
                y = grid_top + run_start * step
                h = (dow - run_start) * step - gap
                parts.append(
                    f'<rect x="{x + 0.75}" y="{y + 0.75}" width="{cell - 1.5}" height="{h - 1.5}" '
                    f'rx="3" fill="none" stroke="{VACATION}" stroke-width="1.5"/>'
                )
                run_start = None

        for dow in range(7):
            d = ws + timedelta(days=dow)
            if d > today or on_vacation(d):
                continue
            info = by_day.get(d.isoformat(), {})
            parts.append(
                f'<rect x="{x}" y="{grid_top + dow * step}" width="{cell}" height="{cell}" rx="3" '
                f'fill="{cell_color(info, mode, max_count)}"><title>{d.isoformat()}: '
                f'{info.get("solvedCount", 0)}문제</title></rect>'
            )

    day_labels = "".join(
        f'<text x="{grid_left - 10}" y="{grid_top + i * step + 10}" class="d" text-anchor="end">{t}</text>'
        for i, t in [(1, "월"), (3, "수"), (5, "금")]
    )

    ly = grid_top + grid_h + 22
    if mode == "level":
        legend_colors, legend_l, legend_r = TIER_GROUP_COLORS, "B", "R"
    else:
        legend_colors, legend_l, legend_r = COUNT_COLORS, "적음", "많음"
    legend = f'<text x="{pad}" y="{ly + 10}" class="d">{legend_l}</text>'
    lx = pad + (30 if mode != "level" else 16)
    legend += f'<rect x="{lx}" y="{ly}" width="{cell}" height="{cell}" rx="3" fill="{EMPTY}"/>'
    for i, c in enumerate(legend_colors):
        legend += f'<rect x="{lx + (i + 1) * step}" y="{ly}" width="{cell}" height="{cell}" rx="3" fill="{c}"/>'
    legend += f'<text x="{lx + (len(legend_colors) + 1) * step + 4}" y="{ly + 10}" class="d">{legend_r}</text>'
    rx = width - pad
    legend += (
        f'<rect x="{rx - 74}" y="{ly + 0.75}" width="{cell - 1.5}" height="{cell - 1.5}" rx="3" '
        f'fill="none" stroke="{VACATION}" stroke-width="1.5"/>'
        f'<text x="{rx}" y="{ly + 10}" class="d" text-anchor="end">스트릭 휴가</text>'
    )

    current = profile.get("currentStreak", 0)
    best = profile.get("maxStreak", 0)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<style>
  text {{ font-family: Pretendard, -apple-system, "Segoe UI", "Noto Sans KR", sans-serif; fill: {TEXT}; }}
  .lbl {{ font-size: 15px; }}
  .big {{ font-size: 40px; font-weight: 800; fill: {GREEN}; }}
  .best {{ font-size: 15px; fill: {SUB}; }}
  .bestn {{ font-size: 20px; font-weight: 700; fill: {SUB}; }}
  .m, .d {{ font-size: 12px; fill: {SUB}; }}
</style>
<defs>
  <linearGradient id="hg" x1="0" x2="1" y1="0" y2="0">
    <stop offset="0" stop-color="{HEADER_BG}"/><stop offset="0.75" stop-color="{HEADER_BG}"/>
    <stop offset="1" stop-color="#1e3328"/>
  </linearGradient>
</defs>
<rect width="{width}" height="{height}" fill="{PAGE_BG}"/>
<rect width="{width}" height="{header_h}" rx="10" fill="url(#hg)"/>
<text x="{pad}" y="{header_h / 2 + 6}" class="lbl">현재</text>
<text x="{pad + 42}" y="{header_h / 2 + 15}" class="big">{current}</text>
<text x="{pad + 54 + len(str(current)) * 24}" y="{header_h / 2 + 6}" class="lbl">일 연속 문제해결</text>
<text x="{width - pad}" y="{header_h / 2 + 7}" text-anchor="end"><tspan class="best">최장</tspan><tspan dx="8" class="bestn">{best}</tspan></text>
<rect y="{card2_y}" width="{width}" height="{card2_h}" rx="10" fill="{CARD_BG}"/>
{"".join(parts)}
{day_labels}
{legend}
</svg>
'''


def main():
    for key in ("SOLVEDAC_HANDLE", "SOLVEDAC_CLIENT_ID", "SOLVEDAC_CLIENT_SECRET"):
        if not os.environ.get(key):
            sys.exit(f"환경 변수 {key}가 비어 있습니다.")

    handle = os.environ["SOLVEDAC_HANDLE"].strip()
    out = os.environ.get("OUTPUT_PATH", "solvedac-streak.svg")
    mode = os.environ.get("STREAK_MODE", "count").strip().lower()
    today = datetime.now(KST).date()
    since = today - timedelta(days=53 * 7)

    h = urllib.parse.quote(handle)
    profile = api_get(f"/users/{h}")
    activity = api_get(f"/users/{h}/activity/days", {"from": since.isoformat(), "to": today.isoformat()})

    with open(out, "w", encoding="utf-8") as f:
        f.write(build_svg(profile, activity, today, mode))
    print(f"{out} 생성 완료 ({mode}): 현재 스트릭 {profile.get('currentStreak')}일")


if __name__ == "__main__":
    main()
