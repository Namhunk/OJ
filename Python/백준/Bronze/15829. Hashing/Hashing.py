a = 96
r = 31
M = 1234567891
L = int(input())
list_alpha = []
sum_list = []
for i in input():
    list_alpha.append(ord(i) % a)
for i in range(L):
    sum_list.append(list_alpha[i] * pow(r, i))
print(sum(sum_list) % M)