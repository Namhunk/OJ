num1 = list(map(int, input()))
num2 = list(map(int, input()))
n = [pow(10, i) for i in range(len(num1))]
result = 0
for i, x in enumerate(num2[::-1]):
    sum = 0
    for j, y in enumerate(num1[::-1]):
        sum += x * y * n[j]
    print(sum)
    result += sum * n[i]
print(result)