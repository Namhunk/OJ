import sys
dic = {key : [] for key in range(1, 201)}
for _ in range(int(sys.stdin.readline().strip())):
    x, y = sys.stdin.readline().strip().split()
    dic[int(x)].append(y)

for i in dic:
    if dic[i] != None:
        for j in dic[i]:
            print(i, j)