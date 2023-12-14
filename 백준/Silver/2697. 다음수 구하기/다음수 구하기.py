import sys

for _ in range(int(sys.stdin.readline().strip())):
    a = int(sys.stdin.readline().strip())
    k = len(str(a))

    for i in range(len(str(a))-1, 0, -1):
        if str(a)[i-1] < str(a)[i]: k = i; break
    
    t = list(str(a)[k-1: ])
    t.sort()
    r = str(a)[:k-1]
    
    for i in range(len(t)):
        if str(a)[k-1] < t[i]:
            r += t[i]
            del t[i]
            break
    
    for i in t:
        r += i
    
    print(int(r) if a != int(r) else "BIGGEST")