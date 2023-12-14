import sys

n = int(sys.stdin.readline().strip())

f = 0
t = 0

if n % 5 == 0: f = n//5
elif (n % 5) % 2 == 0: f = n//5; n %= 5; t = n//2
elif (n % 5) % 2 == 1: f = n//5-1; n -= 5*(n//5-1); t = n//2
print(f+t if f > -1 and t > -1 else -1)