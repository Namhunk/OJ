import sys

def fpow(a, b):
    res = 1
    while b:
        if b & 1: res *= a % c
        a = ((a % c) * (a % c))
        b >>= 1
    return res

a, b, c = map(int, sys.stdin.readline().strip().split())
print(fpow(a, b) % c)