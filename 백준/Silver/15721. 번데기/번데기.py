import sys
input = sys.stdin.readline

from collections import deque
def solve():
    # 게임을 진행하는 사람 A명 (1 <= A <= 2,000)
    A = int(input().strip())

    # 구하고자 하는 번째 T (T <= 100,000)
    T = int(input().strip())

    # 구하고자 하는 구호가 뻔이면 0, 데기면 1로
    R = int(input().strip())

    q = deque([i for i in range(A)])
    n = 1
    cnt = 0
    while 1:
        base = [0, 1, 0, 1]
        temp = [0]*(n+1) + [1]*(n+1)
        base.extend(temp)

        for i in base:
            curr = q.popleft()
            if R == i:
                cnt += 1
            
            if cnt >=  T:
                return curr
            
            q.append(curr)

        n += 1
        
if __name__ == '__main__':
    print(solve())

"""
뻔 = 0, 데기 = 1

1회차 문장
0-1-0-1-0-0-1-1
0-1-0-1-0-0-0-1-1-1

기본 0-1-0-1은 포함,
n이 커질수록 뒤의 부분이 2(n+1)개씩 증가함
"""