import sys, math

n, m = map(int, sys.stdin.readline().strip().split())

k = 1
x2, x5 = 0, 0
while n >= 5**k or n >= 2**k:
    x2 += n // (2**k)
    x5 += n // (5**k)
    k += 1

k = 1
while m >= 5**k or m >= 2**k:
    x2 -= m // (2**k)
    x5 -= m // (5**k)
    k += 1

k = 1
while n-m >= 5**k or n-m >= 2**k:
    x2 -= (n-m) // (2**k)
    x5 -= (n-m) // (5**k)
    k += 1

print(x2 if x2 < x5 else x5)