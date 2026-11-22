import sys, math

for _ in range(int(sys.stdin.readline().strip())):
    m, n, x, y = map(int, sys.stdin.readline().strip().split())
    x -= 1
    y -= 1
    k = x

    while k < m*n:
        if k % n == y:
            print(k + 1)
            break

        k += m
    else:
        print(-1)