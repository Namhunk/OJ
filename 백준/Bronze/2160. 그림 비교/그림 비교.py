import sys
input = sys.stdin.readline

def solve():
    # N(2 <= N <= 50)
    N = int(input().strip())

    arr = [set()] # 그림 정보 저장 배열
    for _ in range(N):
        temp = set() # 각 그림별 임시 저장

        for i in range(5):
            row = list(input().strip())
            for j in range(7):
                if row[j] == 'X': # 현재 위치 값이 X라면
                    temp.add((i, j))
        
        arr.append(temp)
    
    ans = (0, 0) # 정답 변수
    cnt = float('inf')
    # 모든 그림 확인
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            curr = len(arr[i]-arr[j]) + len(arr[j]-arr[i])
            if curr  < cnt:
                cnt = curr
                ans = (i, j)
    
    print(*ans)
        
if __name__ == '__main__':
    solve()
"""
N개의 그림이 있다. 각 그림들은 5x7의 크기, 두가지 색으로 구성(X, .)
그림들이 주어졌을 때 가장 비슷한 두 개의 그림을 찾아라
두 그림에서 다른 칸의 개수가 가장 적을 때 두 개의 그림이 가장 비슷하다.(색칠한 부분이 비슷할 때)

1. 모든 그림의 크기는 같음
2. X가 있는 위치만 추출

"""