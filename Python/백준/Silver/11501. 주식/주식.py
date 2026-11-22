import sys

for i in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    v = list(map(int, sys.stdin.readline().strip().split()))
    p = [v[i] - v[i-1] for i in range(1, n)]
    
    r = c = 0
    for i in range(n-2, -1, -1):
        c += p[i]
        if c < 0: c = 0; 
        else: r += c
    
    print(r)