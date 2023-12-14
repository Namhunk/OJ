list = list(map(int, input().split()))
num = 0
for i in list:
    num += pow(i,2)
print(num % 10)