import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(3)]
cnt = [[0]*3*n for _ in range(3)]
pos = [[0]*3*n for _ in range(2)]

def check_range(a, b, c):
    size = 0
    if a < n: size += 1
    if b < n: size += 2
    if c < n: size += 4

    return size

def MIN(a, b, c):
    size = check_range(a, b, c)
    num = 0
    
    if size == 7: num = min(arr[0][a], arr[1][b], arr[2][c])
    elif size == 6: num = min(arr[1][b], arr[2][c])
    elif size == 5: num = min(arr[0][a], arr[2][c])
    elif size == 4: num = arr[2][c]
    elif size == 3: num = min(arr[0][a], arr[1][b])
    elif size == 2: num = arr[1][b]
    elif size == 1: num = arr[0][a]

    return num

a, b, c = 0, 0, 0
han, yang, jung = 0, 0, 0
idx = 0

while a < n or b < n or c < n:
    num = MIN(a, b, c)
    if a < n and num == arr[0][a]:
        han += 1
        cnt[0][idx] = han
        cnt[1][idx] = yang
        cnt[2][idx] = jung

        a += 1
        pos[0][idx] = 1
        pos[1][idx] = a

        idx += 1
    elif b < n and num == arr[1][b]:
        yang += 1
        cnt[0][idx] = han
        cnt[1][idx] = yang
        cnt[2][idx] = jung

        b += 1
        pos[0][idx] = 2
        pos[1][idx] = b

        idx += 1
    
    elif c < n and num == arr[2][c]:
        jung += 1
        cnt[0][idx] = han
        cnt[1][idx] = yang
        cnt[2][idx] = jung

        c += 1
        pos[0][idx] = 3
        pos[1][idx] = c

        idx += 1

def binary_search(x, y, z, k):
    low, high = 0, 3*n-1
    while low <= high:
        mid = (low + high) // 2

        SUM = min(x, cnt[0][mid]) + min(y, cnt[1][mid]) + min(z, cnt[2][mid])
        if SUM < k: low = mid + 1
        else: high = mid - 1
    
    return low

q = int(sys.stdin.readline().strip())
for _ in range(q):
    x, y, z, k = map(int, sys.stdin.readline().strip().split())
    ans = binary_search(x, y, z, k)

    print(pos[0][ans], pos[1][ans])