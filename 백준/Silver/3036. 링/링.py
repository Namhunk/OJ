import sys, math

n = int(sys.stdin.readline().strip())
ring = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, n):
    print(f'{ring[0] // math.gcd(ring[0], ring[i])}/{ring[i] // math.gcd(ring[0], ring[i])}')
    