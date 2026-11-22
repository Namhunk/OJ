import sys

n, q = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

def x_cnt(x, y): return max(arr[y-1] - x, 0)
def y_cnt(x, y):
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2

        if arr[mid] < x: high = mid
        else: low = mid + 1

    return max(low - y + 1, 0)

for _ in range(q):
    x, y = map(int, sys.stdin.readline().strip().split())

    cnt1 = x_cnt(x, y)
    cnt2 = y_cnt(x, y)

    print(cnt1 + cnt2)