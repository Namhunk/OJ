import sys

n, m = map(int, sys.stdin.readline().strip().split())
S = set(sys.stdin.readline().strip() for _ in range(n))
count = 0
for _ in range(m):
    a = sys.stdin.readline().strip()
    if a in S: count += 1

print(count)