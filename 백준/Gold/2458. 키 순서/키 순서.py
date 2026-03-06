import sys
input = sys.stdin.readline

def solve():
    # 학생 수 N (2 <= N <= 500), 키 비교 횟수 M (0 <= M <= N(N-1)/2)
    N, M = map(int, input().strip().split())
    arr = [[0]*(N+1) for _ in range(N+1)]

    # 두 학생의 크기 비교 a < b
    for _ in range(M):
        a, b = map(int, input().strip().split())
        arr[a][b] = 1
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j or arr[i][j]: continue
            for k in range(1, N+1):
                if arr[i][k] and arr[k][j]:
                    arr[i][j] = 1
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j or arr[i][j]: continue
            for k in range(1, N+1):
                if arr[i][k] and arr[k][j]:
                    arr[i][j] = 1
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j: continue
            if arr[i][j]:
                arr[j][i] = 1
    
    ans = 0
    for i in range(1, N+1):
        if sum(arr[i]) >= N-1:
            ans += 1
    
    return ans

if __name__ == '__main__':
    print(solve())

"""
학생이 N명 있을 때
키가 몇 번째인지 알 수 있는 학생이 몇명인지 계산

해당 노드에 연결된 노드의 수가 힌트

1. i -> k 로 갈 수 있고 k -> j로 갈 수 있다면 i -> j로 갈 수 있음
2. 전체 배열을 돌고 만약 i -> j로 가는 길이 있다면 j -> i 도 가능함
"""