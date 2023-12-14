import sys

n, k, q, m = map(int, sys.stdin.readline().strip().split())
k_list = list(map(int, sys.stdin.readline().strip().split()))
q_list = list(map(int, sys.stdin.readline().strip().split()))

arr = [0]*3 + [-1]*n
for i in k_list:
    if arr[i] < 0: arr[i] *= -1

for i in q_list:
    if arr[i] < 0:
        arr[i] += 1

        for j in range(i*2, n+3, i):
            if arr[j] < 0: arr[j] += 1

for i in range(3, n+3):
    if arr[i] < 0: arr[i] *= -1

    arr[i] += arr[i-1]

for _ in range(m):
    s, e = map(int, sys.stdin.readline().strip().split())

    print(arr[e] - arr[s-1])