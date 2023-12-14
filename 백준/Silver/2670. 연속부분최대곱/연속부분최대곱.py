import sys

n = int(sys.stdin.readline().strip())
arr = [float(sys.stdin.readline().strip()) for _ in range(n)]

for i in range(1, n):
    arr[i] = max(arr[i-1] * arr[i], arr[i])

print(f'{max(arr):.3f}')