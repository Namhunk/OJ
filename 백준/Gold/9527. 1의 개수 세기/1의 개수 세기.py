import sys
input = sys.stdin.readline

# 1의 개수를 세어 출력한다

# 첫줄에 두 자연수 A, B기 주어진다 (1 <= A <= B <= 1e16)
A, B = map(int, input().strip().split())

# 두 자연수 A, B가 주어졌을 때, A <= x <= B를 만족하는 모든 x에 대해 x를 이진수로 표현했을 때 1의 개수의 합을 구해라

# 1e16까지의 각 비트 자릿수
size = len(bin(int(1e16)))-2

# 숫자를 비트로 표시하면 bit[54], bit[53]..., dp[0]의 순서로 표시
# 각 자리수는 2^k ~ 2^(k+1)-1 개의 숫자가 기본으로 있음

# 각 자리수로 구역을 나누면
# dp[0 ~ 53] = [1, 2, 4, 8, 16, 32, 64, ...., ]
# dp[0] = 1 + 0*0 = 1
# dp[1] = 2 + 1*1 = 3
# dp[2] = 4 + 2*2 = 8
# dp[3] = 8 + 3*4 = 20
# dp[4] = 16 + 4*8 = 48
# dp[k] = bit[k] + bit[k-1]*k 의 규칙이 나옴

bit = [0]*size
dp = [0]*size

bit[0], dp[0] = 1, 1
for i in range(1, size):
    bit[i] = (2<<i)-(2<<(i-1))
    dp[i] = bit[i] + bit[i - 1] * i

# 누적합 수행
for i in range(1, size):
    dp[i] += dp[i-1]

dp = [0] + dp # dp[k]는  자릿수 k개의 모든 합
# a, b 값은 2^k의 floor 3 -> 2, 12 -> 8, 17 -> 16

def count(x):
    cnt = 0 # 1의 갯수
    b = bin(x)[2:]
    l = len(b)
    for i in range(l):
        if b[i] == '1': # 해당 위치가 1이면
            temp = l-i-1
            cnt += dp[temp]
            cnt += (x-2**temp+1)
            x = x-2**temp

    return cnt
ans = count(B) - count(A-1)

print(ans)