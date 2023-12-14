import sys

def boyer_moore_majority(arr):
    major = 0
    cnt = 0
    for i in range(1, len(arr)):
        if not cnt:
            major = arr[i]
            cnt += 1
        else:
            if arr[i] == major: cnt += 1
            else: cnt -= 1
    
    check = arr[1:].count(major)
    if check*2 > arr[0]: print(major)
    else: print("SYJKGW")

n = int(sys.stdin.readline().strip())
for _ in range(n):
    arr = list(map(int, sys.stdin.readline().strip().split()))
    boyer_moore_majority(arr)