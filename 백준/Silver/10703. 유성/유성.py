import sys
input = sys.stdin.readline

def solve():
    R, S = map(int, input().split())
    
    arr = [list(input().strip()) for _ in range(R)]
    
    # 각 열에서 가장 낮은 유성 위치와 가장 높은 땅의 위치 찾기
    lowest_X = [-1] * S
    highest_hash = [R] * S  # 땅이 없는 예외를 대비해 R로 초기화
    
    for i in range(R):
        for j in range(S):
            if arr[i][j] == 'X':
                lowest_X[j] = max(lowest_X[j], i)
            elif arr[i][j] == '#':
                highest_hash[j] = min(highest_hash[j], i)
                
    # 유성이 떨어질 수 있는 최대 거리 한 번에 계산
    min_dist = float('inf')
    for j in range(S):
        if lowest_X[j] != -1:  # 해당 열에 유성이 존재한다면
            # 유성의 가장 아래와 땅의 가장 위 사이의 빈 공간 크기
            dist = highest_hash[j] - lowest_X[j] - 1
            min_dist = min(min_dist, dist)
            
    # 모양을 유지하며 새로운 배열에 결과 그리기
    ans = [['.'] * S for _ in range(R)]
    for i in range(R):
        for j in range(S):
            if arr[i][j] == '#':
                ans[i][j] = '#'
            elif arr[i][j] == 'X':
                # 기존 유성의 위치에서 정확히 min_dist만큼만 아래로 이동 (모양 유지)
                ans[i + min_dist][j] = 'X'
                
    # 4. 결과 출력
    for row in ans:
        print(''.join(row))

if __name__ == '__main__':
    solve()