import sys, math

for _ in range(int(sys.stdin.readline().strip())):
    n, m = map(int, sys.stdin.readline().strip().split())
    print(math.factorial(n) // (math.factorial(n-m) * math.factorial(m))
    if n > m else math.factorial(m) // (math.factorial(m-n) * math.factorial(n)))
