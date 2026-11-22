import sys

n = int(sys.stdin.readline().strip())
t = list(map(int, sys.stdin.readline().strip().split()))

t.sort()
m = []
k = n if n % 2 == 0 else n-1
for i in range(k):
    m.append(t[i] + t[k-1-i])

print(max(m))
"""

"""