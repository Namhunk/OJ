import sys

x = int(sys.stdin.readline().strip())
a = x
r = 1
s = 0
c = 0

while a:
    if a & 1: s += r; c += 1
    r *= 2
    a >>= 1

print(c)