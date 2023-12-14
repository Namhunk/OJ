import sys

primes = [False, False] + [True] * (10 ** 7)
nums = []
for i in range(2, len(primes)):
    if primes[i]:
        nums.append(i)
        for j in range(i * i, len(primes), i):
            primes[j] = False

A, B = map(int, sys.stdin.readline().strip().split())
count = 0

for i in nums:
    if  i**2 > B: break
    x = 2
    while i ** x <= B:
        if i ** x >= A: count += 1; x += 1
        else: x += 1

print(count)