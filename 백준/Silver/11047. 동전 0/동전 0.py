import sys

n, k = map(int, sys.stdin.readline().strip().split())
a = [int(sys.stdin.readline().strip()) for _ in range(n)]

a.sort(reverse= True)

r = 0
for i in a:
    if i > k: continue
    if k == 0: break
    r += k//i
    k %= i

print(r)