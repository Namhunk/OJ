import sys

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    k = list(sys.stdin.readline().strip().split())
    
    r = k[0]
    for i in range(1, n):
        if r[0] >= k[i]: r = k[i] + r
        else: r = r + k[i]
    
    print(r)