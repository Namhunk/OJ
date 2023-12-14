import sys

paper = int(sys.stdin.readline().strip())
area = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(paper):
    x, y = map(int, sys.stdin.readline().strip().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            area[j][i] = 1
count = 0
for i in area:
    count += i.count(1)
print(count)