import sys, math

arr = [False, False]  + [True] * (10 ** 5)
primes = []

for i in range(2, len(arr)):
    if arr[i]:
        primes.append(i)
        for j in range(i*2, len(arr), i):
            arr[j] = False

t = int(sys.stdin.readline().strip())
for T in range(1, t+1):
    a, b, n = map(int, sys.stdin.readline().strip().split())
    divisor = []
    for i in primes:
        if i > n: break
        if not (n % i):
            divisor.append(i)
            while not (n % i):
                n //= i
    
    if n != 1: divisor.append(n)
    ans = 0
    for i in range(1, 1 << len(divisor)):
        cnt = 0
        div = 1
        for j in range(len(divisor)):
            if i & (1 << j):
                div *= divisor[j]
                cnt += 1
        
        low = (a-1)//div
        high = b//div
        if low > high: continue
        r = (high-low)
        ans += r if cnt % 2 else -r
    
    print(f'Case #{T}: {b-a+1 - ans}')
