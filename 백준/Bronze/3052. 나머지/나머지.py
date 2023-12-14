list = []
for i in range(10):
    N = (int(input()) % 42)
    if N not in list:
        list.append(N)

print(len(list))