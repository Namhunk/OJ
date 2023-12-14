import sys

K, N = map(int, sys.stdin.readline().strip().split())
line = [int(sys.stdin.readline().strip()) for _ in range(K)]

l = 1
h = (2 ** 31) - 1

while l <= h:
    m = (l + h) // 2
    size = 0

    for i in line:
        size += (i // m)
    
    if size < N: h = m - 1
    elif size > N: l = m + 1
    else:
        l = m + 1

print(h)