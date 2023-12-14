X = int(input())
sum = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b

if X == sum: print("Yes")
else: print("No")