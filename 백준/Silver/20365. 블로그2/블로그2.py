import sys

n = int(sys.stdin.readline().strip())
color = sys.stdin.readline().strip()
b = 0
r = 0
s = color[0]

for i in range(1, n):
    if s[-1] == color[i]:
        s += color[i]
    
    else:
        if s[-1] == "B": b += 1
        else: r += 1
        s = color[i]
if s[-1] == "B": b += 1
else: r += 1

print(r + 1 if b > r else b + 1)