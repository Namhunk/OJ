import sys
arr = []
for _ in range(int(sys.stdin.readline().strip())):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr.append((y, x))

arr.sort()
for y, x in arr:
    print(x,y)