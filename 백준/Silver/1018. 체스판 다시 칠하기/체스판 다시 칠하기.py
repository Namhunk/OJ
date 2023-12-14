import sys
N, M = map(int, sys.stdin.readline().strip().split())
chess = [sys.stdin.readline().strip() for _ in range(N)]
count = []
chess_list = []
for i in range(N-7):
    for j in range(M-7):
        a = []
        for k in range(i, i+8):
            a.append(chess[k][j: j+8])
        chess_list.append(a)

for i in chess_list:
    a = 0; b = 0
    for x in range(8):
        for y in range(8):
            if (x+y) % 2 == 1 and i[x][y] != 'W':
                a += 1
            elif (x+y) % 2 != 1 and i[x][y] == 'W':
                a += 1
            if (x+y) % 2 != 0 and i[x][y] != 'B':
                b += 1
            elif (x+y) % 2 == 0 and i[x][y] == "B":
                b += 1
    count.append(b if a > b else a)

print(min(count))