list_T = []
for i in range(int(input())):
    list_T.append(sum(map(int, input().split())))

for i,j in enumerate(list_T, start=1):
    print(f'Case #{i}: {j}')