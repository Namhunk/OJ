import sys
input = sys.stdin.readline

from collections import deque
def solve(r1, r2, c1, c2): # 현재 검사할 종이의 범위
    cnt = {-1: 0, 0: 0, 1: 0} # 각 숫자들의 개수를 저장
    
    # 현재 범위가 1x1일때까지
    if (r2-r1)//3 <= 0 and (c2-c1)//3 <= 0:
        cnt[arr[r1][c1]] += 1
        return cnt
    else:
        d = (r2-r1)//3
        for i in range(3):
            nc1, nc2 = c1+d*i, c1+d*(i+1)
            for j in range(3):
                nr1, nr2 = r1+d*j, r1+d*(j+1)
                for k, v in solve(nr1, nr2, nc1, nc2).items(): # 3x3으로 나눈 값들의 개수 count
                    cnt[k] += v
        
        # 만약 -1, 0, 1 중 하나의 값만 0이 아닌 경우 (1)조건을 만족함
        zero_cnt = 0
        idx = 2
        for i in range(-1, 2):
            if cnt[i] == 0:
                zero_cnt += 1
            else:
                idx = i
        
        if zero_cnt == 2:
            cnt[idx] = 1
                
        return cnt

if __name__ == '__main__':
    # N (1 <= N <= 3**7, N = 3**k)
    N = int(input().strip())

    # 종이안의 값
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    visit = [[0]*N for _ in range(N)] # 방문 및 개수를 저장할 배열
    for _, v in solve(0, N, 0, N).items():
        print(v)
    

"""
종이 크기는 N x N, 각 종이의 칸에는 -1, 0, 1 중 하나가 저장

(1). 종이가 모두 같은 수라면 그대로 사용
(2). (1)이 아닌 경우 종이를 같은 크기의 종이 9개로 자르고, 각 종이에 대해 (1)의 과정을 반복

종이를 잘랐을때 -1, 0, 1로 채워진 각 종이의 개수를 구해라

1. 종이가 주어졌을 때 3 x 3으로 나눔(3x3으로 나눌 수 없을 때까지 수행)
2. 3x3으로 나눈 종이의 전체 숫자들을 확인함
3. 만약 종이 안의 숫자가 서로 다르다면 각 번호들의 대한 개수를 반환함, -1, 0, 1 = a, b, c
4. 만약 모두 같은 숫자라면 그 숫자에 대한 개수만 올려주고 나머지는 0으로 반환

"""