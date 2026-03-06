import sys
input = sys.stdin.readline

def solve():
    # 학생 수 N (2 <= N <= 500), 키 비교 횟수 M (0 <= M <= N(N-1)/2)
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]

    # 두 학생의 크기 비교 a < b
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
    
    # 1. 플로이드-워셜 알고리즘 (루프 순서: k -> i -> j)
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if arr[i][k]:  # 최적화: i에서 k로 가는 길이 있을 때만 내부 루프 실행
                for j in range(1, N + 1):
                    if arr[k][j]:
                        arr[i][j] = 1
    
    # 2. 자신의 키 순서를 알 수 있는 학생 카운트
    ans = 0
    for i in range(1, N + 1):
        known_count = 0
        for j in range(1, N + 1):
            if i == j:
                continue
            # i가 j보다 작거나(arr[i][j]) 크거나(arr[j][i]) 비교가 가능하면 카운트
            if arr[i][j] or arr[j][i]:
                known_count += 1
        
        # 나를 제외한 모든 학생(N-1명)과 비교가 가능하다면 순서를 알 수 있음
        if known_count == N - 1:
            ans += 1
            
    return ans

if __name__ == '__main__':
    print(solve())
