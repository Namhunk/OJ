import sys

def check(a, b, c):
    cnt = 0
    for i in range(len(a)):
        cnt += (a[i] != b[i]) + (b[i] != c[i]) + (c[i] != a[i])
    
    return cnt

def run(n, arr):
    if n > 16 * 2:
        return 0
    
    ans = 1e9
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                ans = min(ans, check(arr[i], arr[j], arr[k]))
    
    return ans

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    arr = list(sys.stdin.readline().strip().split())
    print(run(n, arr))
