import sys

def fibo(fibonums, n):
    fibonums.append(fibonums[n-2]+fibonums[n-1])
    return fibonums
fibonums = [0, 1]

n = int(sys.stdin.readline().strip())

if n < 2: print(fibonums[n])
else:
    for i in range(2, n+1):
        fibo(fibonums, i)
    
    print(fibonums[-1])