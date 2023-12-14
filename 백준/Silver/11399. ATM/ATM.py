import sys

n = int(sys.stdin.readline().strip())
p = list(map(int, sys.stdin.readline().strip().split()))

p.sort()
s = 0
m = []
for i in p:
    s += i
    m.append(s)

print(sum(m))