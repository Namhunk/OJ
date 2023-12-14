import sys

N, M = map(int, sys.stdin.readline().strip().split())
H = list(map(int, sys.stdin.readline().strip().split()))

l = 0
h = max(H)

while l <= h:
    length = 0
    m = (l + h) // 2

    for i in H:
        if i > m:
            length += (i-m)
        if length > M: break
    if length < M: h = m - 1
    elif length > M: l = m + 1
    else: l = m + 1

print(h)