import sys

num =[]
for _ in range(7):
    i = int(sys.stdin.readline().strip())
    if i%2==1: num.append(i)

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(min(num))