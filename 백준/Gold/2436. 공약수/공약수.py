import sys
input = sys.stdin.readline

from itertools import combinations
def solve():
    # A, B (2 <= A, B <= 100,000,000)
    A, B = map(int, input().strip().split())

    MAX_SIZE = B//A
    
    # MAX_SIZE를 구성하는 모든 소수의 값들을 구함
    NUMS = []
    i = 2
    while MAX_SIZE > 1:
        if MAX_SIZE % i == 0:
            MAX_SIZE //= i
            NUMS.append(i)
        else:
            i += 1

    # 각 중복되는 숫자들을 곱함
    TEMP = [NUMS[0] if len(NUMS) else 1]
    for i in range(1, len(NUMS)):
        if NUMS[i] == NUMS[i-1]:
            TEMP[-1] *= NUMS[i]
        
        else:
            TEMP.append(NUMS[i])
    
    # TMEP의 각 숫자들에 대해 2개의 그룹으로 분리하는 모든 경우를 구함
    # 이때 두 자연수의 차이를 최소화 하는 방향으로

    ans = []
    for i in range(len(TEMP)):
        for j in combinations(TEMP, i):
            a = 1
            for k in j:
                a *= k
            
            b = B//(A*a)
            ans.append((a+b, A*a, A*b))
    
    ans = sorted(ans)
    print(*ans[0][1:])
    
if __name__ == '__main__':
    solve()

"""
두 자연수 A, B가 주어졌을 때 A를 최대공약수, B를 최소공배수로 하는 두 개의 자연수
여러 개가 있는 경우 두 자연수의 합이 최소가 되는 값을 구해라

1. 최대 공약수 G를 갖기 위해서 두 자연수 모두 G를 포함해야 함
    Gn, Gm

2. 최소 공배수 L을 갖기 위해서 두 자연수는 서로소 여야 함
    각 자연수는 서로 겹치지 않는 소수의 곱으로 표현이 가능해야 함

---------
B // A 의 값을 사용

이때 나오는 각 소수들을 모두 사용


"""