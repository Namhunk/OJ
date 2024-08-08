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

dp = [[[float('inf')]*5 for _ in range(5)] for _ in range(len(seq))]
dp[0][0][0] = 0

for i in range(len(seq)):
    if seq[i] == 0: break
    for l in range(5):
        for r in range(5):
            dp[i+1][seq[i]][r] = min(dp[i+1][seq[i]][r], dp[i][l][r]+move(l, seq[i]))
            dp[i+1][l][seq[i]] = min(dp[i+1][l][seq[i]], dp[i][l][r]+move(r, seq[i]))

ans = min([min(i) for i in dp[-1]])
print(ans)