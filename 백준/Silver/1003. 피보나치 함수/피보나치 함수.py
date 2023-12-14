import sys

def fibonacci(x):
    if cnt[x][0] < 0 and cnt[x][1] < 0:
        cnt[x] = [fibonacci(x-1)[0] + fibonacci(x-2)[0], fibonacci(x-1)[1] + fibonacci(x-2)[1]]
    
    return cnt[x][0], cnt[x][1]

cnt = [[1, 0], [0, 1]] + [[-1, -1] for _ in range(39)]
T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    print(*fibonacci(N))