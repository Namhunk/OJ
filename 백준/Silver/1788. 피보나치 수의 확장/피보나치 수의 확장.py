import sys

arr = [0, 1] + [0] * (999999)
for i in range(2, len(arr)):
    arr[i] = (arr[i-1] + arr[i-2]) % 10**9


n = int(sys.stdin.readline().strip())
if n == 0: print(0)
elif n < 0 and n % 2 == 0: print(-1)
else: print(1)
print(arr[abs(n)])