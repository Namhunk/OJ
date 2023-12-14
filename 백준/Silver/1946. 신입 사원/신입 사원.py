import sys


t = int(sys.stdin.readline().strip())
for _ in range(t):
    c = 0
    l = [0] * 100001
    n = int(sys.stdin.readline().strip())

    for _ in range(int(n)):
        a, b = map(int, sys.stdin.readline().strip().split())
        l[a] = b
    
    for i in range(1, n):
        if l[i] < l[i+1]: c += 1; l[i+1] = l[i]
    
    print(n - c)
