import sys

n, q = map(int, sys.stdin.readline().strip().split())
s = list(sys.stdin.readline().strip())

red, blue = [], []
for i in range(n):
    if s[i] == 'R': red.append(i)
    if s[i] == 'B': blue.append(i)

def lower_bound(l, arr):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2

        if arr[mid] < l: low = mid + 1
        else: high = mid
    
    return high

def upper_bound(r, arr):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2

        if arr[mid] <= r: low = mid + 1
        else: high = mid
    
    return high

for _ in range(q):
    l, r = map(int, sys.stdin.readline().strip().split())

    a = lower_bound(l, red)
    b = upper_bound(r, red)
    c = lower_bound(l, blue)
    d = upper_bound(r, blue)

    b -= 1; d -= 1

    if b-a < 1 or d-c < 1: print(-1); continue
    if red[a+1] >= blue[d-1]: print(-1); continue

    print(red[a], red[a+1], blue[d-1], blue[d])
