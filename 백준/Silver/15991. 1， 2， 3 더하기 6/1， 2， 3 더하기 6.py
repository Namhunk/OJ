import sys

arr = [[0, 0, 0] for _ in range(100001)]
arr[1] = [1, 0, 0]
arr[2] = [1, 1, 0]
arr[3] = [1, 0, 1]
for i in range(4, 100001):
    if i % 2 == 0:
        arr[i][0] = sum(arr[i-1]) % (10**9 + 9)
        arr[i][1] = arr[i-1][0] % (10**9 + 9)
        arr[i][2] = arr[i-1][1] % (10**9 + 9)
    else:
        arr[i] = arr[i-1]

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(sum(arr[n]) % (10**9 + 9))