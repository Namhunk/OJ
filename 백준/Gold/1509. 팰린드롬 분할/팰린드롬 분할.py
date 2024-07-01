import sys

# 다른 사람들의 코드를 참고함
# 문자열을 펠린드롬으로 분할했을 때, 분할 개수의 최솟값 출력
S = list(sys.stdin.readline().strip())
L = len(S)
P = [[0]*L for _ in range(L)] # 펠린드롬 확인 배열
dp = [2500 for _ in range(L+1)]
dp[-1] = 0

for i in range(L): # 최소 펠린드롬 길이 1
    P[i][i] = 1

for i in range(L-1): # 길이가 다음 문자가 같은지 비교
    if S[i] == S[i+1]:
        P[i][i+1] = 1

for l in range(3, L+1): # 현재 길이
    for start in range(L-l+1): # 3~L 까지 펠린드롬인지 확인
        end = start+l-1
        if S[start] == S[end] and P[start+1][end-1]: # 두 문자가 같고 사이가 펠린드롬이면 펠린드롬
            P[start][end] = 1

for end in range(L): # 
    for start in range(end+1):
        if P[start][end]:
            dp[end] = min(dp[end], dp[start-1]+1)
        else:
            dp[end] = min(dp[end], dp[end-1] + 1)

print(dp[L-1])