import sys

n = int(sys.stdin.readline().strip())
rank = [int(sys.stdin.readline().strip()) for _ in range(n)]
rank.sort()

r = 0
for i in range(n):
    r += abs(i+1 - rank[i])

print(r)