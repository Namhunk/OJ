import sys
input = sys.stdin.readline

# 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 오름차순으로 출력
# 전체 용액의 수 N (2 <= N <= 100,000)
N = int(input().strip())
# 용액의 특성값 sol (-1,000,000,000 <= sol[i] <= 1,000,000,000)
sol = sorted(list(map(int, input().strip().split())))

result = 2e9 # 최소 값 저장
l, r = 0, N-1
ans = [sol[l], sol[r]]
while l < r: # 양 끝에서 부터 0에 가까운 두 용액의 특성값을 찾음
    SUM = sol[l] + sol[r]

    if abs(SUM) < result: # 현재 용액의 값이 작으면
        result = abs(SUM) # 최소값 변경
        ans = [sol[l], sol[r]] # 정답
    if SUM < 0: l += 1 # 0에 가까워 지도록 음수면 양수 방향, 양수면 음수 방향으로 이동
    elif SUM > 0: r -= 1
    else: break

print(*ans)