import sys
dic = []
for _ in range(int(sys.stdin.readline().strip())):
    x, y = map(int, sys.stdin.readline().strip().split())
    dic.append([x,y])
for x,y in dic:
    c = 1
    for i, j in dic:
        if x < i and y < j: c += 1
    print(c, end=' ')