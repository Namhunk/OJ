list = []
max = 0
num = 0
for i in range(1,10):
    list.append(int(input()))
    if list[i - 1] > max:
        max = list[i - 1]
        num = i

print(max)
print(num)