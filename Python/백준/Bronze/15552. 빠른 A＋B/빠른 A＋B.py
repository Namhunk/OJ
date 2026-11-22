import sys
list_T = []
for i in range(int(sys.stdin.readline().strip())):
    A, B = map(int, sys.stdin.readline().strip().split())
    list_T.append(A + B)
for i in list_T:
    print(i)