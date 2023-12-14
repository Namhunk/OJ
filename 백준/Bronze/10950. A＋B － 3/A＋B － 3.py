T = int(input())
list = []
for i in range(T):
    list.append(sum(map(int, input().split())))

for i in list:
    print(i)