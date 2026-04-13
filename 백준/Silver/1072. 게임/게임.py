import sys
input = sys.stdin.readline

def solve():
    # X, Y (1 <= X <= 1,000,000,000, 0 <= Y < = X)
    X, Y = map(int, input().strip().split())
    
    base = (Y*100) // X # 다음 게임을 수행하기 전의 승률
    if base >= 99: return -1

    ans = 0
    for i in range(len(str(X)), -1, -1):
        l, r = 0, 10
        while l < r:
            m = (l + r) // 2

            temp = ans + m*10**i
            curr = ((Y+temp)*100) // (X+temp)
            if curr <= base: l = m+1
            else: r = m
        
        ans += (l-1)*10**i

    while base >= ((Y+ans)*100) // (X+ans):
        ans += 1
    
    return ans

if __name__ == '__main__':
    print(solve())

"""
게임 횟수 : X
이긴 게임 : Y (Z%)
Z는 승률, 소수점은 버린다. X = 53, Y = 47 이면 Z = 88

첫째 줄에 게임을 최소 몇 판 더 해야하는지 출력한다. 만약 Z가 절대 변하지 않는다면 -1을 출력

Y가 증가하고 X도 증가함
X, Y가 동시에 증가할때 어떤 지점에서 변화가 생기는지
Y는 X보다 작음

1. X, Y에 a 라는 숫자를 더할때 최소가 되는 a를 구함
2. 10^i 위치마다 검사 i의 최대 길이는 X의 자릿수 개수
3. 이분탐색으로 현재 위치에 어떤 숫자가 와야 기준값을 넘기는지 확인

1,000,000,000
  470,000,000

19,230,770
18,888,888
"""