import sys

n = int(sys.stdin.readline().strip())
zoo = [[1] * 3] + [[0] * 3 for _ in range(n-1)]

for i in range(1, n):
    zoo[i][0] = (zoo[i-1][1] + zoo[i-1][2]) % 9901
    zoo[i][1] = (zoo[i-1][0] + zoo[i-1][2])  %9901
    zoo[i][2] = sum(zoo[i-1]) % 9901

print(sum(zoo[n-1]) % 9901)
