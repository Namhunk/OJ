import sys
input = sys.stdin.readline

from math import gcd
def solve():
    # (1 <= X, Y, P1, P2 <= 100)
    X, Y, P1, P2 = map(int, input().strip().split())

    if abs(P1-P2) % gcd(X, Y) != 0:
        print(-1)
    else:
        i = 0
        while P1 != P2:
            if P1 < P2:
                P1 += X
            else:
                P2 += Y
    
        print(P1)
        
if __name__ == '__main__':
    solve()

"""
두 사람 A, B가 일직선상 트랙에서 같은 방향으로 멀리뛰기를 하고 있음
A는 한 번에 X미터, B는 한 번에 Y미터를 뜀
시작 지점, X, Y가 주어졌을때 두 학생이 공통적으로 지나는 지점 중 시작점에서 가장 가까운 지점을 찾아라
없다면 -1

XN + P1 = YM + P2 가 되는 지점을 찾아야 함
XN-YM = P2-P1

이때 X, Y는 두 수의 곱으로 구성됨
1x1, 1x2, 2x1, ...

N, M에는 같을수도 다를수도 있는 두 숫자가 들어감

예제 1
10N + 30 = 12M + 8
10N-12M = -22
2(5N-6M) = -2(11)

예제 2
N + 7 = M + 12
1(N-M) = 1(5)

예제 3
7N + 2 = 7M + 1
7(N-M) = -1

XN - YM = P2-P1
위 식이 성립하려면

(XN-YM), (P2-P1)이 동일한 공약수를 가져야 함
좌변이 항상 짝수, 우변이 항상 홀수라면 성립할 수 없기 때문

G(XN-YM) = G(P2-P1)

"""