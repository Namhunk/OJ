A = int(input())
B = int(input())
C = int(input())
list = [A, B, C]
mul = 1
for i in list:
    mul *= i

mul = str(mul)
print(mul.count("0"))
for i in range(1, 10):
    print(mul.count(str(i)))