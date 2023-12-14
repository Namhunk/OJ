import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

if M:
    button = set(sys.stdin.readline().strip().split())
else:
    button = set()

ans = abs(N - 100)

for i in range(int(1e6)+1):
    for j in str(i):
        if j in button:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i-N))

print(ans)