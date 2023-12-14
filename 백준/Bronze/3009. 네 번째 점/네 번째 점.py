import sys
x = []
y = []
for _ in range(3):
    a, b = map(int, sys.stdin.readline().strip().split())
    if a not in x: x.append(a)
    else: x.remove(a)
    if b not in y: y.append(b)
    else: y.remove(b)

print(*x, *y)