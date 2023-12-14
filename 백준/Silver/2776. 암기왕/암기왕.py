import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    arr1 = list(map(int, sys.stdin.readline().strip().split()))

    dict = {arr1[i]: 1 for i in range(n)}

    m = int(sys.stdin.readline().strip())
    arr2 = list(map(int, sys.stdin.readline().strip().split()))

    for i in range(m):
        print(dict.get(arr2[i], 0))