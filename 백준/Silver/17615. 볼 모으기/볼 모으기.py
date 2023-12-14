import sys

n = int(sys.stdin.readline().strip())
ball = sys.stdin.readline().strip()

t = [1]
for i in range(1, n):
    if ball[i-1] != ball[i]:
        t.append(1)
    else:
        t[-1] += 1

x = [0, 0]
if len(t) % 2 == 1:
    for i in range(len(t)-1) if t[0] < t[-1] else range(1, len(t)):
        x[i % 2] += t[i]
    
else:
    for i in range(1, len(t)-1):
        x[i%2] += t[i]
    
print(x[0] if x[0] < x[1] else x[1])