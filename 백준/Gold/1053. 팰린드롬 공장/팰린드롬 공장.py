import sys
input = sys.stdin.readline

# 문자열이 주어졌을 떄, 팰린드롬으로 만들기 위해 필요한 연산의 최솟값을 출력

# 연산 4가지
#   1. 문자열의 어떤 위치에 어떤 문자를 삽입(시작과 끝도 가능)
#   2.어떤 위치에 있는 문자를 삭제
#   3.어떤 위치에 있는 문자를 교환
#   4.서로 다른 문자를 교환

# 4번 연산은 최대 1번, 나머지는 무제한

def Palindrome(s, i, j):
    if dp[i][j] != float('inf'):
        return dp[i][j]

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            break

    if i >= j:
        return 0

    res = min(Palindrome(s, i+1, j)+1,
              Palindrome(s, i, j-1)+1,
              Palindrome(s, i+1, j-1)+1)
    dp[i][j] = res
    return res

# 문자열 입력 (최대 길이 50)
S = list(input().strip())
size = len(S)
dp = [[float('inf') for _ in range(size)] for _ in range(size)]
ans = Palindrome(S, 0, size-1) # 교체 x

from itertools import combinations
idx_pair = list(combinations([i for i in range(size)], 2))

for i, j in idx_pair:
    dp = [[float('inf') for _ in range(size)] for _ in range(size)]  # 초기화
    S[i], S[j] = S[j], S[i]
    ans = min(ans, Palindrome(S, 0, size-1) + 1)
    S[i], S[j] = S[j], S[i]

print(ans)