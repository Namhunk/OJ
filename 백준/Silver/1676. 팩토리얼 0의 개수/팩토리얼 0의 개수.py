import sys, math

n = int(sys.stdin.readline().strip())
num = str(math.factorial(n))
c = 0
for i in num[::-1]:
    if i == '0': c += 1
    else: break

print(c)