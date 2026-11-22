import sys

nums = [False, False] + [True] * (2 * 123456 - 1)
primes = []
for i in range(2, len(nums)-1):
    if nums[i]:
        primes.append(i)
        for j in range(2*i, len(nums)-1, i):
            nums[j] = False

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0: break
    else:
        count = 0
        for i in primes:
            if n < i <= 2 * n: count += 1
            elif i > 2 * n: break
        print(count)