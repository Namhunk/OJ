import sys
N, r, c = map(int, sys.stdin.readline().strip().split())
arr = [0]*2**N
arr[0], arr[1] = 0, 3
for i in range(1, N):
    now = 2**i
    arr[now] = now**2*3
    for j in range(1, now):
        arr[now+j] = arr[now] + arr[j]

r_num = arr[r]//3*2
c_num = arr[c]//3
print(r_num+c_num)