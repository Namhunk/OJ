import sys

n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

s = sum(a) // n
r = 0
for i in range(n-1):
    if a[i] > s:
        r += (a[i]-s)
        a[i+1] += (a[i]-s)
    
    else:
        r += (s-a[i])
        a[i+1] -= (s-a[i])

print(r)