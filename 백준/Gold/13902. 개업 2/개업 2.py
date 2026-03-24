import sys
input = sys.stdin.readline

def solve():
    # N (1 <= N <= 10,000), M(1 <= M <= 1,000)
    N, M = map(int, input().strip().split())

    # 웍의 크기 S (1 <= S[i] <= N) M개
    S = list(map(int, input().strip().split()))

    # 한번의 행동에 요리할 수 있는 모든 그릇의 크기
    cook = set() # 요리를 1회만 할 때 그릇들의 크기를 저장(중복 x)
    for i in range(M):
        if S[i] > N: continue
        # 1개만 사용
        cook.add(S[i])
        for j in range(i+1, M):
            if S[i] + S[j] > N: continue
            # 2개 사용
            cook.add(S[i] + S[j])
    
    cook = sorted(cook) # 오름차순 정렬
    
    dp = [float('inf')]*(N+1)
    dp[0] = 0
    for c in cook:
        for j in range(c, N+1):
            if dp[j-c] + 1 < dp[j]:
                dp[j] = dp[j-c] + 1
    
    if dp[N] == float('inf'):
        print(-1)
    else:
        print(dp[N])
    
if __name__ == '__main__':
    solve()

"""
주문 받은 짜장면의 수와 가지고 있는 웍의 크기가 주어질 때
최소 몇 번의 요리로 모든 주문을 처리할 수 있는지
모든 주문을 처리할 수 없는 경우 -1 출력

동시에 두개의 웍으로 요리를 할 수 있음

1. 1개 또는 2개를 사용할때 나올수 있는 그릇의 개수를 먼저 구함
2. 1 부터 N까지 모든 횟수들을 채워나감(임시로 1차원 배열)
    - 

0 1 2 3 4 5 6
0 1 2 3 4 5 6
0 1 2 1 2 3 2
0 1 2 1 1 2 2
"""