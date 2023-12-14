N = int(input())
list = list(map(int, input().split()))
max = max(list)
for i in range(N):
    list[i] = list[i] / max * 100

print(f'{sum(list) / N } ')