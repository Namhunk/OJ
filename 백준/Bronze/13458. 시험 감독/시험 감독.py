import sys, math

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
b, c = map(int, sys.stdin.readline().strip().split())

s = n
for i in a:
    if i-b > 0: s += math.ceil((i-b)/c)

print(s)