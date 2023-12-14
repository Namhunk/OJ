import sys

n, m = map(int, sys.stdin.readline().strip().split())
a = list(map(int, sys.stdin.readline().strip().split()))
b = list(map(int, sys.stdin.readline().strip().split()))

ap = 0
bp = 0
ans = []

while ap < n and bp < m:
    if a[ap] <= b[bp]: ans.append(a[ap]); ap += 1
    else: ans.append(b[bp]); bp += 1

if ap == n: ans.extend(b[bp:])
else: ans.extend(a[ap:])

print(*ans)