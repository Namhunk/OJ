import sys, math

m = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

rpow = [i*i  for i in range(int(math.ceil(m**0.5)), int(math.floor(n**0.5))+1)]

if len(rpow) > 0:
    print(sum(rpow))
    print(min(rpow))
else:
    print(-1)