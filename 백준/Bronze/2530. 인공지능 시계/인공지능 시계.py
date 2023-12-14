import sys

a,b,c = map(int, sys.stdin.readline().strip().split())
s = int(sys.stdin.readline().strip())
c += s
if c >= 60: b += c//60; c %= 60
if b >= 60: a += b//60; b %= 60
print(a%24, b, c)