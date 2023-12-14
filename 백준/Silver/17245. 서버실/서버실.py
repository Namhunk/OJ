import sys

n = int(sys.stdin.readline().strip())
arr = []
half = 0
for _ in range(n):
    computer = list(map(int, sys.stdin.readline().strip().split()))
    arr.append(computer)
    half += sum(computer)

half /= 2
ans = int(1e7)
low, high = 0, int(1e7)
while low <= high:
    SUM = 0
    mid = (low + high) // 2

    for i in range(n):
        for j in range(n):
            if arr[i][j]: SUM += min(arr[i][j], mid)
    
    if SUM >= half: high = mid - 1; ans = min(ans, mid)
    else: low = mid + 1

print(ans)