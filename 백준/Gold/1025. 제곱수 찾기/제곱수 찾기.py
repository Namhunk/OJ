import sys
input = sys.stdin.readline

# 만들 수 있는 가장 큰 완전 제곱수 출력
# 만들 수 없는 경우에는 -1 출력
# 1 <= N, M <= 9
# 최대 9자리
# i, j 는 한 방향으로만 움직일 수 있음

def solv(x, y, i, j, a, b):
    global ans
    nums = arr[x][y]

    i *= a
    j *= b
    while 1:
        if int(nums)**0.5 == int(int(nums)**0.5):
            ans = max(ans, int(nums))

        if not (0 <= x+i < N and 0 <= y+j < M): break

        x += i
        y += j
        nums += arr[x][y]

N, M = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(N)]
ans = -1
if int(arr[0][0]) ** 0.5 == int(int(arr[0][0]) ** 0.5):
    ans = max(ans, int(arr[0][0]))
for x in range(N):
    for y in range(M):
        for i in range(N):
            for j in range(M):
                if (i, j) == (0, 0): continue
                solv(x, y, i, j, 1, 1)
                solv(x, y, i, j, -1, 1)
                solv(x, y, i, j, 1, -1)
                solv(x, y, i, j, -1, -1)
print(ans)

