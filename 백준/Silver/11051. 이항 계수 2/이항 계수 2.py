import sys, math

n, k = map(int, sys.stdin.readline().strip().split())
print(math.factorial(n) // (math.factorial(n-k) * math.factorial(k)) % 10007)