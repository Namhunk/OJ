import sys

def fact(n):
    if n <= 1: return 1
    return n * fact(n-1)

N = int(sys.stdin.readline().strip())

print(fact(N))