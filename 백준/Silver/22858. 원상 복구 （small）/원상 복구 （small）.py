import sys
input = sys.stdin.readline

def solve():
    # N, K (1 <= N <= 10^4, 1 <= K <= 10^3)
    N, K = map(int, input().strip().split())

    S = [0]+list(map(int, input().strip().split()))
    D = [0]+list(map(int, input().strip().split()))

    for _ in range(K):
        temp = [0]*(N+1)
        for i in range(N, 0, -1):
            temp[D[i]] = S[i]
        
        S = temp
    
    print(*S[1:])
            
if __name__ == '__main__':
    solve()

"""
N개의 카드가 있고 이 카드들은 P[i]의 값을 가짐
1-N 의 수가 적힌 D가 존재 할 때 D[i]번째 카드를 i번쨰로 가져오는게 셔플이라 함

K번 셔플한 카드의 정보와 D를 알고 있다 할 때 원래 카드는 어떤 배치인지 출력

셔플은 교환이 아닌 위치로 전송하는 방식

단순 반복문으로 수행하기에는 시간이 오래 걸릴것으로 보임

우선 단순 방법으로 제출 해봄
"""