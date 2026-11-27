import sys
import random, math
input = sys.stdin.readline

def get_cnt(N, L, M, X, A):
    k, cur, cnt = 0, 0, 0
    for i in range(N):
        if cur == 0: # 아무것도 없는경우
            k = i

        if i - k + 1 > L: # L 길이를 넘기는 경우 초기화를 시킴
            cnt +=  1
            cur = 0
            k = i

        cur += A[i]

        if cur > X:
            cnt += (cur // X)
            cur %= X
            k = i

        if cnt > M: # 도중에 M을 넘기면 빠져나옴
            return cnt
        
    if cur:
        cnt += 1

    return cnt

    
def solve(N, M, L, A):
    lo, hi = 1, sum(A)

    if get_cnt(N, L, M, hi, A) > M: # X의 크기를 전체 합 크기로 했을때도 안되면 -1
        return -1

    while lo < hi:
        X = (lo + hi) // 2

        if get_cnt(N, L, M, X, A) <= M:
            hi = X

        else:
            lo = X + 1

    return lo

def main():
    # (1 <= L, N <= 10**5), (1 <= M <= 10**15)
    N, M, L = map(int, input().strip().split())

    # 0 <= A[i] <= 10**10
    A = list(map(int, input().strip().split()))

    print(solve(N, M, L, A))

if __name__ == '__main__':
    main()  

"""
도로는 1 ~ N까지의 구역으로 나뉨, i번 구역에는 A[i]만큼 눈이 쌓임
제설도구는 성능 X가 있고, 성능 X인 제설도구는 1회 사용 시 L개 이하의 연속한 구간을 골라
총합 X이하의 눈을 제거할 수 있다

*모든 눈을 치우기 위한 X의 최솟값* 치울 수 없다면 -1을 출력


1. 도구 X는 M회 사용 가능
2. 도구 X는 L개 이하의 연속한 구간을 골라 X만큼 지울 수 있음
----------------------------------------------------

"""