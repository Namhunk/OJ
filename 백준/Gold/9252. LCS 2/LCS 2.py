import sys
input = sys.stdin.readline

# 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를, 둘째 줄에 LCS를 출력
# LCS가 여러 가지인 경우에는 아무거나 출력하고 LCS의 길이가 0인 경우에는 둘째 줄을 출력하지 않는다

S1 = list(input().strip()) # 입력 문자열 1
S2 = list(input().strip()) # 입력 문자열 2

dp = [[0]*(len(S2)+1) for _ in range(len(S1)+1)] # LCS 배열
for i in range(1, len(S1)+1): # LCS 수행
    for j in range(1, len(S2)+1):
        if S1[i-1] == S2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

ans = [] # LCS 문자 배열
x, y = len(S1), len(S2)
while x > 0 and y > 0: # LCS 역추적 (i-1, j-1) == (i, j)인 경우만 저장
    if dp[x][y] == dp[x-1][y]: x -= 1 
    elif dp[x][y] == dp[x][y-1]: y -= 1
    else:
        ans.append(S1[x-1])
        x -= 1
        y -= 1

cnt = dp[len(S1)][len(S2)]
print(cnt)
if cnt:
    print(''.join(reversed(ans)))