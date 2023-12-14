import sys

A, B = map(int, sys.stdin.readline().strip().split())
K, X = map(int, sys.stdin.readline().strip().split())


low = K - X
high = K + X

if high < A or low > B: print("IMPOSSIBLE")
else:
    ans1 = max(low, A)
    ans2 = min(high, B)
    print(ans2 - ans1 + 1)
