import sys

def find(left, mid, right):
    global idx1, idx2, idx3, MIN
    while mid < right:
        SUM = arr[left] + arr[mid] + arr[right]
        if abs(SUM) < abs(MIN):
            MIN = SUM
            idx1, idx2, idx3 = left, mid, right
        
        if SUM < 0: mid += 1
        elif SUM > 0: right -= 1
        else: return 1
    
    return 0

n = int(sys.stdin.readline().strip())
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))

MIN = float('inf')
idx1, idx2, idx3 = 0, 0, 0

for left in range(n-2):
    if find(left, left + 1, n-1): break
    

print(arr[idx1], arr[idx2], arr[idx3])