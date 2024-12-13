import sys
input = sys.stdin.readline

# 첫째 줄에 정답을 기약분수 형태로 출력한다. p/q 꼴로 출력하며, p는 분자, q는 분모이다. 정답이 0인 경우에는 0/1로,
# 1인 경우에는 1/1로 출력한다

# 첫째 줄에 집합의 수의 개수 N이 주어진다. (1 <= N <= 15)
N = int(input().strip())

# 둘째 줄부터 N개의 줄에는 집합에 포함된 수가 주어진다. 각 수의 길이는 길어야 50인 자연수
arr = [int(input().strip()) for _ in range(N)]

# 마지막 줄에는 K가 주어진다.(1 <= K <= 100)
K = int(input().strip())

# 기약 분수 형태로 만들기 위한 gcd 연산
def gcd(a, b):
    while a != 0:
        if a < b:
            a, b = b, a

        a %= b
    return b

# 각 DP 의 값은 각 숫자들을 합쳤을 때 나머지가 x인 (x <= K) 값들의 개수
dp = [[0] * K for _ in range(1 << N)] # 행은 각 숫자의 사용 여부를 나타내므로 2^N, 열은 나머지 이므로 0-K
dp[0][0] = 1 # 아무 숫자도 고르지 않은 경우는 1개

# 모든 집합의 숫자들에 대해, K 보다 작은 나머지 값들을 만났을 때에 대한 값을 미리 계산해 둠
mod_nums = []
for i in range(N): # 집합의 모든 값들에 대해
    temp = []
    for j in range(K): # K 보다 작은 나머지 값을 만났을 때에 대한 값들
        temp.append((j * (10 ** len(str(arr[i])) % K) + (arr[i] % K)) % K)
    mod_nums.append(temp)

for i in range(1 << N): # 모든 자리수 조합
    for j in range(N): # 모든 숫자
        if i & (1 << j): # 현재 조합에 j에 해당되는 숫자가 포함되있다면
            continue # 수행을 건너 뜀

        for k in range(K): # 모든 나머지들에 대해
            next_mod = mod_nums[j][k] # 위 반복문에서 j 번째 숫자의 나머지 k와 연산한 값
            dp[i | (1 << j)][next_mod] += dp[i][k] # DP[다음에 포함할 숫자][다음 나머지] 는 += DP[현재 포함된 숫자][현재 나머지]  

p = dp[-1][0]
q = sum(dp[-1])
g = gcd(p, q)
print(f'{p//g}/{q//g}')
"""
DP, 비트마스킹을 사용, 외판원 순회문제?
https://velog.io/@kevin622/BOJ-1086-%EB%B0%95%EC%84%B1%EC%9B%90

아이디어
arr = 순열 {13, 19}, K = 3 이라고 할 때
13 % K = 1, 19 % K = 1
1319 % K는 13의 나머지인 1에 10**len(19)를 곱하고 19의 나머지인 1을 더한 값에 % K로 나눈 값과 같다.

DP + 비트 마스킹은 각 위치의 요소를 0 또는 1로 표현, 만약 13, 2, 11 인 순열이 있다고 할 때
각 숫자의 사용 여부를 0 또는 1로 나타냄 
2만 사용한 경우 = 010, 13, 11을 사용한 경우 = 101, 13, 2를 사용한 경우 = 110

"""