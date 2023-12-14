import sys

n, k = map(int, sys.stdin.readline().strip().split())

if n < k: print(0)
else:
    r = 0
    while bin(n).count('1') > k:
        r += n&(-n)
        n += n&(-n)
    
    print(r)