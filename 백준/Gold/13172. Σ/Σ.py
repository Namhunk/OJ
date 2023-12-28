import sys

# 모든 주사위를 한 번씩 던졌을 때 나온 숫자들의 합의 기댓값을 출력.
# 답을 기약분수로 나타냈을 때 a/b 가 되면, (a x b^-1) mod (int(1e9)+7)을 출력
# b^-1 은 b의 모듈러 곱셈에 대한 역원

# 기약분수 형태로 만들기 위한 함수(최대 공약수를 구함)
def gcd(a, b):
    while a and b:
        if a > b: a %= b
        else: b %= a
    
    return max(a, b)

# 분할정복을 사용한 거듭제곱 함수
def power(n, x):
    if x == 1: return n
    elif x % 2: return n * power(n, x-1) % X
    temp = power(n, x//2)
    return temp * temp % X
    
# 주사위의 수를 나타내는 정수 M(1 <= M <= 1e4)
M = int(sys.stdin.readline().strip())

# M개의 줄에 각 주사위의 정보
# i(1 <= i <= M)번째 줄에는 Ni, Si(1 <= N, S <= int(1e9))가 공백으로 구분되 주어짐
X = int(1e9)+7 # mod 할 값
ans = 0 # 정답

for _ in range(M): # M 번의 반복을하면서
    N, S = map(int, sys.stdin.readline().strip().split()) # Ni, Si 값 받음
    # S / N 형태를 만들어주기 위해 최소 공배수를 구함
    d = gcd(N, S)
    
    # N, S 를 기약분수 형태로 만들어주기 위해 최소 공배수 d로 N, S를 나눔
    N //= d
    S //= d
    
    # mod 값을 구함
    mod = power(N, X-2)
    ans = (ans + (mod * S % X)) % X

print(ans)