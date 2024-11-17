import sys
input = sys.stdin.readline

N = int(input().strip())
arr = sorted(map(int, input().strip().split()))
x = 2
mod = int(1e9)+7
ans = 0

for i in range(1, N):
    ans += ((arr[i] - arr[N-1-i]) * (x-1)) % mod
    x = (x * 2) % mod

print(ans % mod)