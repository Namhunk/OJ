import sys
input = sys.stdin.readline

def solve():
    # N (1 <= N <= 1,000)
    N = int(input().strip())

    snack = [int(input().strip()) for _ in range(N)]
    dp = [0]*N

    for i in range(N):
        dp[i] = snack[i]

        for j in range(i):
            if snack[j] < snack[i]:
                dp[i] = max(dp[i], dp[j] + snack[i])
    
    print(max(dp))

if __name__ == '__main__':
    solve()


"""
간식 파티 계획표의 최대 만족도를 출력

N일동안 간식 파티가 열림

파티의 만족도 = 파티가 열리는 동안 먹은 모든 간식의 평점의 합

간식을 먹을수도 or 먹지 않을수도 있음, 간식은 하루에 하나만 지급
전에 먹었던 간식보다 더 맛있는 간식을 먹어야만 한다

9
3 1 2 5 3 4 5 6 7

9
3 
1 
2 
5 
3 
4
5 
6 
7
"""