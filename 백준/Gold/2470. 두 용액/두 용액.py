import sys

n = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))

left, right = 0, n-1
idx1, idx2 = 0, n-1
Sum = 2*1e9
while left < right:
    liquid = arr[left] + arr[right]
    if abs(liquid) < Sum:
        Sum = abs(liquid)
        idx1 = left
        idx2 = right
    
    if liquid < 0: left += 1
    elif liquid > 0: right -= 1
    else: break

print(arr[idx1], arr[idx2])