import sys

N = int(sys.stdin.readline().strip())

if N != 1:
    k = 2
    while N != 1:
        if N % k == 0: N /= k; print(k)
        else: k += 1