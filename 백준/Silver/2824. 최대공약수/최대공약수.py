import sys, math

n = int(sys.stdin.readline().strip())
nl = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
ml = list(map(int, sys.stdin.readline().strip().split()))

a = 1
b = 1
for i in nl:
    a *= i
for i in ml:
    b *= i

r = math.gcd(a,b)
print(r if len(str(r)) < 10 else str(r)[len(str(r))-9:])
    