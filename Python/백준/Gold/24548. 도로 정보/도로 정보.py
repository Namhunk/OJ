import sys

n = int(sys.stdin.readline().strip())
data = list(sys.stdin.readline().strip())

t, g, f, p = 0, 0, 0, 0
dp = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(3)]
dp[0][0][0][0] = 1

ans = 0
for i in data:
    if i == 'T': t = (t + 1) % 3
    elif i == 'G': g = (g + 1) % 3
    elif i == 'F': f = (f + 1) % 3
    elif i == 'P': p = (p + 1) % 3

    ans += dp[t][g][f][p]
    dp[t][g][f][p] += 1

print(ans)