N = int(input())
listN = list(map(int, input().split()))
max = listN[0]
min = listN[N - 1]
for i in range(N):
    if listN[i] > max: max = listN[i]
    if listN[i] < min: min = listN[i]
print(min,max)