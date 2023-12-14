import sys

def fpow(a, b):
    res = 1
    while b:
        if b & 1: res *= (a % 10)
        a = ((a % 10)*(a % 10))
        b >>= 1
    return res

for _ in range(int(sys.stdin.readline().strip())):
    a, b = map(int, sys.stdin.readline().strip().split())
    r = fpow(a, b) % 10
    if r == 0: print(10)
    else: print(r)