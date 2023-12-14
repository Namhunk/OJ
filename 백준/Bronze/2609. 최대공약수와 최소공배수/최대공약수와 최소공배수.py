a, b = map(int, input().split())
list_i = []
k = 2
min = 1
for i in range(1, a+1 if a <= b else b+1):
    if a % i == 0 and b % i == 0: list_i.append(i)
while k <= a and k <= b:
    if a % k == 0 and b % k == 0:
        a //= k
        b //= k
        min *= k
    else: k += 1
print(max(list_i))
print(a * b * min)