import sys
input = sys.stdin.readline

# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.
# 둘째 줄에는 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력한다.

# LIS 문제

# 수열의 A의 크기 N(1 <= N <= 1,000,000)
N = int(input().strip())
# 수열 A를 이루고 있는 A[i] (-1,000,000,000 <= A[i] <= 1,000,000,000)
A = list(map(int, input().strip().split()))

record = [0]*N # A[0] ~ A[N-1]의 각 원소들에 대해 최장 길이를 저장하는 배열
dp = [A[0]] # 임시 저장 배열
record[0] = 1

for i in range(1, N):
    if dp[-1] < A[i]: # 다음 값이 최대 값 보다 크면
        dp.append(A[i]) # 배열에 추가
        record[i] = len(dp) # 현재 길이 입력

    else:
        l, r = 0, len(dp)-1
        while l < r:
            m = (l+r)//2
            if dp[m] < A[i]: l = m+1
            else: r = m

        dp[l] = A[i]
        record[i] = l+1

# LIS를 담을 배열
ans = []
cnt = len(dp)
# Refer to https://ggam-nyang.tistory.com/40
# 최대 dp를 가지는 수 부터 역으로 하나씩 담는다. 그 이후 reverse하여 출력
# 더 작은 dp(LIS 길이)를 가지고, 더 작은 인덱스를 가지는 것들을 연결하여 담으면, 무조건 LIS가 완성된다.

for i in range(N-1, -1, -1): # 역순으로 탐색
    if record[i] == cnt:
        ans.append(A[i])
        cnt -= 1

    if cnt < 1: break

print(len(ans))
print(*ans[::-1])