n = int(input())
i = 0
num = n
while True:
    a = n // 10
    b = n % 10
    c = (a + b) % 10
    n = (b * 10) + c
    i += 1
    if num == n:
        break

print(i)