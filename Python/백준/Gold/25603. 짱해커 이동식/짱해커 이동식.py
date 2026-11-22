import sys

n, k = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

ans = 0
start = 0
while True:
    MIN = 0
    for i in range(start, start + k):
        if i >= n: print(ans); exit()
        if arr[i] <= ans: start = i+1; MIN = arr[i]
    
    if not MIN: ans = min(arr[start: start + k])
