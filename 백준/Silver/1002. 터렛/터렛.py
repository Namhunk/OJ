import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
    distance = ((x2-x1)**2+(y2-y1)**2)**0.5
    if distance == r1 == r2 == 0: print(1)
    elif not distance and r1 == r2: print(-1)

    elif distance == r1+r2: print(1)

    elif distance and distance == abs(r1-r2): print(1)

    elif abs(r1-r2) < distance < r1+r2: print(2)

    else: print(0)