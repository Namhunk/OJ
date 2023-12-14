import sys

m = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))

a, b = 1, 1
ans = 0
for i in range(m):
    if i == 0: continue

    if p[i-1] > p[i]:
        a += 1
        ans = max(ans, b)
        b = 1
    elif p[i-1] < p[i]:
        b += 1
        ans = max(ans, a)
        a = 1
    
ans = max(ans, a, b)
print(ans)
"""


"""