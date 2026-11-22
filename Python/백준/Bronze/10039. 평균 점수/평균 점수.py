import sys

s = 0
for _ in range(5):
    i = int(sys.stdin.readline().strip())
    if i < 40:
        s+= 40
    else: s+=i
print(s // 5)