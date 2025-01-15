import sys
input = sys.stdin.readline

# 각각의 테스트 케이스에 대해서 k가 합성수라면 k를 포함하는 소수 사이 수열의 길이를 출력. 그렇지 않으면 0 출력

primes = []
visit = [0]*2 + [1]*(1300000)
for i in range(2, len(visit)):
    if visit[i]:
        primes.append(i)
        for j in range(2*i, len(visit), i):
            visit[j] = 0

def upper(x):
    l, r = 0, len(primes)
    while l < r:
        m = (l + r) // 2
        if primes[m] <= x:
            l = m+1
        else:
            r = m

    return l

def lower(x):
    l, r = 0, len(primes)
    while l < r:
        m = (l + r) // 2
        if primes[m] < x:
            l = m+1
        else:
            r = m

    return l

# 테스트 케이스의 개수 T
T = int(input().strip())

# 각 T개의 줄에 정수 k 입력
for _ in range(T):
    k = int(input().strip()) # k가 소수가 아니라면 두 소수 사이 범위 안에 들어감
    l = upper(k)
    r = lower(k)
    print(primes[r] - primes[l-1])
