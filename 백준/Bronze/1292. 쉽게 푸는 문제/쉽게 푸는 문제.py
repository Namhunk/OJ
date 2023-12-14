import sys

a, b = map(int, sys.stdin.readline().strip().split())

ss = 0
se = 0

k_e = 0

k_s = 0
for i in range(1, 46):
    ss += i
    k_s += (i * i)
    if ss >= a:
        z_s = (k_s -i * (ss - (a - 1)))
        break


for i in range(1, 46):
    se += i
    k_e += (i * i)
    if se >= b:
        s_e = (k_e - i * (se - (b)))
        break

print(s_e - z_s)