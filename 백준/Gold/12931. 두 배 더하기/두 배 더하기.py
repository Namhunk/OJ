import sys
input = sys.stdin.readline

def solve(N, B):
    cnt = 0 # 수행 횟수
    idx = 0 # 0이 아닌 최솟값의 위치
    for i in range(N):
        if B[i] == 0:
            idx = i + 1
    
    while idx < N: # B의 모든 값이 0이 되기 전까지
        for i in range(idx, N):
            if B[i] % 2 == 1: # 해당 값이 홀수라면
                B[i] -= 1 # -1 수행
                cnt += 1  # 횟수 +1
                if B[i] == 0:
                    idx = i + 1

        if idx < N:
            for i in range(idx, N):
                B[i] //= 2
                if B[i] == 0:
                    idx = i+1
            
            cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    # N (1 <= N < = 50)
    N = int(input().strip())

    # B[i] (0 <= B <= 1,000)
    B = sorted(list(map(int, input().strip().split()))) # 편의상 오름차순 정렬
    solve(N, B)


"""
길이 N인 배열 A에 모든 값이 0으로 채워져 있을때
1. 배열에 있는 값 하나를 1증가 시킴
2. 배열에 있는 모든 값을 x2 시킴

배열 B가 주어졌을때 배열  A를 B로 만들기 위한 연산의 최소 횟수를 구해라

------------------------------------------------
1. B에서 홀수인 값들에 대해 -1을 모두 수행
2. 1을 수행하면 짝수만 남음 이때 전체를 2로 나눠줌
3. 1 -> 2 반복

"""