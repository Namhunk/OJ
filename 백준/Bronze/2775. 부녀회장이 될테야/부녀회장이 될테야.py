room = [[None for i in range(14)] for i in range(15)]
for i in range(14):
    room[0][i] = i + 1
for i in range(1, 15):
    for j in range(14):
        room[i][j] = sum(room[i - 1][:j + 1])
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(room[k][n-1])