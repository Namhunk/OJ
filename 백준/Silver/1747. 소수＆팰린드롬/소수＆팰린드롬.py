import sys, math

primes = [False , False] + [True] * 1500000
for i in range(2, int(math.sqrt(len(primes)))+1):
    if primes[i]:
        for j in range(i*i, len(primes), i):
            primes[j] = False

N = int(sys.stdin.readline().strip())

for i in range(N, len(primes)):
    if primes[i]:
        if str(i) == str(i)[::-1]: print(i); break
