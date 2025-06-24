import sys

# 언어에는 단어가 N개 있다.
# 언어의 문장은 단어를 공백없이 붙여 쓴다.
# 문장에서 각 단어는 0번 또는 그 이상 나타날 수 있다
# 단어에 쓰여 있는 문자의 순서를 바꿔도 된다.
# 원래 단어의 위치와 다른 위치에 있는 문자의 개수 만큼이 그 순서를 바꾼 단어를 만드는 비용이다.

# 주어진 문장을 해석할 때 여러 가지 방법 중 비용의 최솟값을 구해라.
# 문장을 해석할 수 없다면 -1 출력

# 문장이 주어진다. 문장의 길이 최대 50
S = " "+input().strip()

# 단어의 개수 N입력 (1 <= N <= 50)
N = int(input().strip())

# 각 N개의 단어 입력
W = [input().strip() for _ in range(N)]

# 문장과 단어는 알파벳 소문자로만 이루어짐

def check(sen, word): # 현재 문장과 단어의 비용을 계산 / 두 길이는 같아야 함
    ret = 0
    for i in range(len(sen)):
        if sen[i] != word[i]:
            ret += 1

    return ret

dp = [[float('inf')]*(len(S)) for _ in range(len(S))] # 비용의 최솟값을 저장하는 배열
dp[0][0] = 0

for i in range(1, len(S)+1):
    if dp[i-1][0] == float('inf'): continue
    for word in W:
        l = len(word)
        if sorted(S[i:i+l]) == sorted(word): # 같은 길이의 문자들을 정렬했을때 구성이 같은지
            dp[i][i+l-1] = min(dp[i][i+l-1], dp[i-1][0]+check(S[i:i+l], word))
            dp[i+l-1][0] = min(dp[i+l-1][0], dp[i][i+l-1])

if dp[-1][0] != float('inf'):
    print(dp[-1][0])
else:
    print(-1)
