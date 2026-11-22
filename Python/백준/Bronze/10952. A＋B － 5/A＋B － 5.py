list_T = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    list_T.append(a + b)

for i in list_T:
    print(i)