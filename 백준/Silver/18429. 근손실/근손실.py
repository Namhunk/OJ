import sys
input = sys.stdin.readline

from itertools import permutations
def solve():
    # N, K 입력 (1<= N <= 8, 1<= K <= 50)
    N, K = map(int, input().strip().split())

    # 각 키트의 중량 증가량 입력 (1 <= A[i] <= 50)
    A = list(map(int, input().strip().split()))

    ans = 0
    # 사전에 길이 N의 모든 조합을 만들어냄
    for seq in permutations(A): 
        weight = 0
        flag = 1
        cnt = 0
        for i in seq:
            weight += i
            cnt += 1

            if weight < K*cnt:
                flag = 0
                break
        
        if flag:
            ans += 1
    
    return ans

if __name__ == '__main__':
    print(solve())
    


"""
- 하루가 지날 때마다 중량이 K만큼 감소, K = 4일때 중량이 488로 감소
- 운동 키트는 사용할때마다 중량이 증가, 각 운동 키트는 고유함
- 각 운동 키트는 N일 동안 1번씩만 사용 가능
- 각 키트는 하루에 1번씩만 사용 가능
- N일동안 중량이 항상 500 이상으로 유지가 되어야 함

운동 기간동안 항상 중량이 500 이상이 되도록 하는 경우의 수

N, K의 범위는 매우 작음
모든 경우를 탐색해도 문제는 없어 보임

D 가 1부터 N까지 증가한다고 할 때 D = 각 날짜
현재까지 거쳐온 A[D]들의 합이 K * D 보다 커야 함

길이 N의 배열에 대해 사전에 모든 조합을 만들고 확인해 보는 방법
"""