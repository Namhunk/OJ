import sys

n, k = map(int, sys.stdin.readline().strip().split())
nums = list(i for i in range(1, n+1))
r = []

for i in range(n-1, 0 , -1):
    if k == 0:
        break

    if k >= i:
        r.append(i)
        k -= i

for i in range(len(r)):
    nums.remove(r[i]+1)
    nums.insert(i, r[i]+1)

print(*nums)