import sys
N = int(sys.stdin.readline().strip())
Nlist = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
Mlist = list(map(int, sys.stdin.readline().strip().split()))
Nlist.sort()

for i in Mlist:
    a = 0
    b = len(Nlist)
    while a < b:
        m = (a+b) // 2
        if Nlist[m] < i: a = m+1
        elif Nlist[m] > i: b = m
        elif Nlist[m] == i: print(1); break
    if Nlist[m] != i: print(0)