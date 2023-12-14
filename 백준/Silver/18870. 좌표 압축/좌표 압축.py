import sys

N = int(sys.stdin.readline().strip())
X = list(map(int, sys.stdin.readline().strip().split()))
Y = sorted(set(X))

Z = {Y[i] : i for i in range(len(Y))}

for i in X:
    print(Z[i], end=" ")