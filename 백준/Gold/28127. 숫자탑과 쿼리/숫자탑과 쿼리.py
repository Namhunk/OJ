import sys

def findx(a, d, x):
    first, last = 1, a
    floor = 1

    while True:
        if first <= x <= last: return (floor, x-first+1)

        first = last+1
        last = floor * d + last + a
        floor += 1


q = int(sys.stdin.readline().strip())
for _ in range(q):
    a, d, x = map(int, sys.stdin.readline().strip().split())
    print(*findx(a, d, x))