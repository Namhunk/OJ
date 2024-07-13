import sys
input = sys.stdin.readline
from math import sqrt
# 자연수 N이 연속된 소수의 합으로 나타낼 수 있는 경우의 수 (1 <= N <= 4e6)
# 소수는 한번씩만 사용 가능

# 소수들의 누적합을 구해서 합이 N과 같은지 검사
MAX = int(4e6) # N의 최대 범위
visit = [False]*2 + [True]*(MAX-1) # 소수 체크
primes = [0] # 소수를 담는 배열

# 에라토스테네스의 체
for i in range(2, MAX+1):
    if visit[i]:
        primes.append(i)
        for j in range(2*i, MAX+1, i):
            visit[j] = False

for i in range(1, len(primes)): primes[i] += primes[i-1] # 소수 누적합

N = int(input().strip()) # N 입력
ans = 0
l, r = 0, 1
while l < r and r < len(primes):
    curr = primes[r]-primes[l]
    if curr < N: r += 1
    elif curr > N: l += 1
    else: ans += 1; r += 1

print(ans)