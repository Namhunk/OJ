import sys, collections

n, k = map(int, sys.stdin.readline().strip().split())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))

ans = 0
current, temp = 0, 0
Dict = collections.defaultdict(int)
for i in range(1, n+1):
    current += arr[i]
    temp = current - k * i

    ans += Dict[temp]
    Dict[temp] += 1

print(ans + Dict[0])
