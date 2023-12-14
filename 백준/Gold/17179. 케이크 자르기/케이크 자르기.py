import sys

n, m, l = map(int, sys.stdin.readline().strip().split())
s = list(int(sys.stdin.readline().strip()) for _ in range(m)) + [l]

for _ in range(n):
    q = int(sys.stdin.readline().strip())

    low, high = 1, int(4 * 1e6)
    ans = 0
    while low <= high:
        mid = (low + high) // 2

        cnt = 0
        prev = 0

        for cut in s:
            if cut - prev >= mid:
                cnt += 1
                prev = cut
        
        if cnt > q: low = mid + 1; ans = max(ans, mid)
        else: high = mid - 1
    
    print(ans)
