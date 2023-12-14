import sys

for _ in range(int(sys.stdin.readline().strip())):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    Count = 0
    for _ in range(int(sys.stdin.readline().strip())):
        cx, cy, r = map(int, sys.stdin.readline().strip().split())
        if (x1-cx)**2 + (y1-cy)**2 < r**2 and (x2-cx)**2 + (y2-cy)**2 > r**2: Count+=1
        elif (x1-cx)**2 + (y1-cy)**2 > r**2 and (x2-cx)**2 + (y2-cy)**2 < r**2: Count+=1

    print(Count)