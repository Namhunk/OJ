import sys
arr = []
for _ in range(int(sys.stdin.readline().strip())):
    x, y = map(int, sys.stdin.readline().strip().split())
    arr.append((x,y))

arr.sort()
for x, y in arr:
    print(x,y)