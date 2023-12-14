import sys, math

for _ in range(int(sys.stdin.readline().strip())):
    x, y = map(int, sys.stdin.readline().strip().split())
    k = int(math.sqrt(y-x))

    if k**2 == y-x: print(2*(k-1)+1)
    elif k**2 < y-x <= k*(k+1): print(2*k)
    elif k*(k+1) < y-x < (k+1)**2: print(2*k+1)