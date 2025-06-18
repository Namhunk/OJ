import sys

# 목적을 당성하기 위해 피룡한 카드 섞는 횟수의 최솟값

def card_shuffle(N, P, S): # 카드를 섞는 함수, arr = 현재 P의 배치 상태
    tmp = [0]*N

    for i in range(N):
        tmp[S[i]] = P[i]

    return tmp

def check(N, P):
    tmp = [0]*N
    for i in range(0, N, 3):
        if (P[i], P[i+1], P[i+2]) != (0, 1, 2):
            return 0

    return 1

def solve():
    # N 입력 ( 3 <= N <= 48, N은 3의 배수) (카드는 0 ~ N-1번)
    N = int(input().strip())

    # 길이가 N인 수열 P
    P = list(map(int, input().strip().split()))

    # 길이가 N인 수열 S
    S = list(map(int, input().strip().split()))

    if check(N, P):
        return 0

    cnt = 0
    visit = set() # 현재 P 값들의 순서를 저장할 집합
    visit.add(tuple(P))
    while not check(N, P):
        P = card_shuffle(N, P, S)
        if tuple(P) in visit: # 중복된다면 -1
            return -1
        visit.add(tuple(P))
        cnt += 1

    return cnt

print(solve())

"""
각 플레이어의 수는 3
각 플레이어는 0, 1, 2 순서로 카드를 가져감
카드를 섞기를 최소로 해서 P의 순서가 0, 1, 2로 반복되게 바꿔야 함
i번째 카드는 S[i]번째 위치로 이동함

S[i] 값은 항상 고정
P[i]의 순서만 계속 변함

최종적으로 P의 순서가 0 1 2 라면 종료
순서가 변하지 않는다면 -1 출력

while 종료 조건

i == S[i] 라면 -1
N은 3의 배수, 3개씩 묶었을 때 각 자리의 합을 (N//3)으로 나눴을 때 0 1 2가 나오는지

"""