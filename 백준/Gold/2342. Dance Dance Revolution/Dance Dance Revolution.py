import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
# 한 줄에 모든 지시 사항을 만족하는데 사용되는 최소의 힘을 출력

# 중점: 0, 위: 1, 왼쪽: 2, 아래: 3, 오른쪽: 4
# 시작을 제외하고 두 발은 같은 지점에 있으면 안됨
# 중앙 -> 다른 지점으로 이동 = 2의 힘을 사용
# 다른 지점 -> 인접한 지점 = 3의 힘을 사용
# 다른 지점 -> 반대편 = 4의 힘을 사용
# 같은 지점을 한번 더 누름 = 1의 힘을 사용
# 두 발은 동시에 움직이지 않음

# 지시 사항 입력, 각 수열은 1, 2, 3, 4의 숫자로 이루어짐, 0은 마지막을 의미, 수열의 길이는 100,000을 넘지 않음
seq = list(map(int, input().strip().split()))

# 움직임 함수
def move(a, b):
    if a == b: return 1
    elif a == 0: return 2
    elif abs(b-a) % 2 == 0: return 4
    else: return 3

def solve(n, l, r):
    global dp
    if n >= len(seq)-1: return 0

    if dp[n][l][r] != -1:
        return dp[n][l][r]

    dp[n][l][r] = min(solve(n+1, seq[n], r) + move(l, seq[n]),
                      solve(n+1, l, seq[n]) + move(r, seq[n]))
    return dp[n][l][r]

dp = [[[-1]*5 for _ in range(5)] for _ in range(len(seq))]
print(solve(0, 0, 0))