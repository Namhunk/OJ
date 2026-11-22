import sys

N = int(sys.stdin.readline().strip())
A = set(map(int, sys.stdin.readline().strip().split()))

num = 1
for i in A:
    n = 0
    for j in range(2, max(A)):
        if i != j and i % j == 0: n = 1; break
    if n == 0:
        num *= i
print(num if num != 1 and num < 2 ** 63 else -1)