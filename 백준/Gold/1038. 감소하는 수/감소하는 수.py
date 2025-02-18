import sys
input = sys.stdin.readline

# N번째 감소하는 수를 출력, 없으면 -1

# N (0 <= N <= 1,000,000)
N = int(input().strip())

# 모든 경우를 먼저 구해봄
arr = []

def solve(x):
    s = (x % 10) - 1

    for i in range(s, -1, -1):
        num = x*10+i
        arr.append(num)
        solve(num)

for i in range(10):
    arr.append(i)
    solve(i)

arr.sort()

if len(arr) > N:
    print(arr[N])
else:
    print(-1)