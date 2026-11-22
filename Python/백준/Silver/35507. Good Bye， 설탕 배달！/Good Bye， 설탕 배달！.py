import sys
input = sys.stdin.readline

def solution():
    # 1 <= N <= 300,000
    N = int(input().strip())
    arr = []
    # 0 <= a[i], b[i], c[i] <= 10**18
    # 1 <= p[i] <= 10**18
    # p[i] <= p[i+1]
    bp = 0
    remain = 0
    state = [0, 0, 0]
    ans = 'YES'
    for _ in range(N):
        # a, b, c, p
        row = list(map(int, input().strip().split())) # 요구 조건
        curr = row[3] + remain - bp - 1 # p일차 + 이전 나머지 - 이전 p = 사용 가능 일 수
        for i in range(3): # a, b, c 검사
            if state[i] >= row[i]: # 현재 보유한 값이 요구 값 이상인 경우 패스
                continue
            else: # 부족한 경우
                curr -= (row[i]-state[i]) # 필요한 만큼 뺴줌
                state[i] = row[i]
        
        if curr < 0: ans = 'NO' # 모든 계산이 끝나고 현재 값이 음수면 NO
        else: # 값이 남았다면
            bp = row[3]
            remain = curr

    return ans

if __name__ == '__main__':
    # 1 <= T <= 300,000
    T = int(input().strip())
    for _ in range(T):
        print(solution())

"""
N개의 문제로 구성된 문제집의 i번째는 지금보다 지식이 a[i] 더 필요, 구현력 b[i] 더 필요
사고력 c[i] 더 필요

하루를 사용해 안 푼 문제 하나를 품 or
지식을 1 쌓거나, 구현력을 1 올리거나, 사고력을 1 키움

i번째 문제를 적어도 p[i]일차까지 해결하려 함

계획을 지킬 수 있다면 YES, 없다면 NO

하루에 a, b, c 중 하나만 + 1 가능

초기값
0 0 0
첫 p[0] 이 4일때
p[0]-1 = 3을, a, b, c 중 하나에 분배 가능


0 0 0 0
2 1 0 4
3 > 3 + 0

2 1 0 4
3 3 1 12

7 > 7

"""