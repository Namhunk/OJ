import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))

Dict = {0: 1}
current, ans = 0, 0

for i in range(n):
    current += a[i]

    if current % m in Dict: ans += Dict[current % m]; Dict[current % m] += 1
    else: Dict[current % m] = 1

print(ans)