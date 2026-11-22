import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(2)]

pos = [[0, 0] for _ in range(2*n)]
cnt = [[0, 0] for _ in range(2*n)]

x, y, idx, han, yang = 0, 0, 0, 0, 0
while x < n or y < n:
    if y >= n or (x < n and arr[0][x] <= arr[1][y]):
        han += 1
        cnt[idx][0] = han
        cnt[idx][1] = yang
        pos[idx][0] = 1
        x += 1
        pos[idx][1] = x
        idx += 1
    
    elif x >= n or (y < n and arr[1][y] < arr[0][x]):
        cnt[idx][0] = han
        yang += 1
        cnt[idx][1] = yang
        pos[idx][0] = 2
        y += 1
        pos[idx][1] = y
        idx += 1

def binary_search(i, j, k):
    low, high = 0, 2*n-1
    while low <= high:
        mid = (low + high) // 2
        temp = min(i, cnt[mid][0]) + min(j, cnt[mid][1])
        if temp < k: low = mid + 1
        else: high = mid -1
    
    return low

q = int(sys.stdin.readline().strip())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    ans = binary_search(i, j, k)
    print(pos[ans][0], pos[ans][1])