import sys

N, M, B = map(int, sys.stdin.readline().strip().split())
land = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
T = 500 * 500 * 2 * 256
H = 0
for h in range(257):
    b = B
    t = 0
    for i in land:
        for j in i:
            if j > h:
                b += (j - h)
                t += (2 * (j - h))
            elif j < h:
                b -= (h - j)
                t += (h - j)
    if b < 0: break
    else:
        if t <= T and h >= H:
            T = t; H = h

print(T, H)