import sys

for i in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    l = list(map(int, sys.stdin.readline().strip().split()))
    l.sort()
    tl = []
    tr = []

    for i in range(n):
        if i % 2 == 0: tl.append(l[i])
        else: tr.append(l[i])
    
    l = tl + tr[::-1]
    m = 0
    for i in range(1, n):
        if abs(l[i-1]-l[i]) > m: m = abs(l[i-1]-l[i])
    
    print(m)
