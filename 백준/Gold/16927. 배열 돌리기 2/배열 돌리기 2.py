import sys
input = sys.stdin.readline

def solve(N, M, R):
    # (1 <= A[i][j] <= 10**8)
    A = [list(map(int, input().strip().split())) for _ in range(N)]

    # 정답을 저장할 배열
    arr = [[0]*M for _ in range(N)]

    MIN = min(N, M) # N, M 둘 중 더 작은 숫자는 2의 배수임

    for i in range(MIN//2):
        # 각 위치의 범위는 (i, N-i-1), (i, M-i-1) 임
        n, m = N-i, M-i
        
        key2idx = {}
        idx2key = []

        for x in range(i, n-1):
            key2idx[(x, i)] = len(idx2key)
            idx2key.append((x, i))
        
        for y in range(i, m-1):
            key2idx[(n-1, y)] = len(idx2key)
            idx2key.append((n-1, y))
        
        for x in range(n-1, i, -1):
            key2idx[(x, m-1)] = len(idx2key)
            idx2key.append((x, m-1))
        
        for y in range(m-1, i, -1):
            key2idx[(i, y)] = len(idx2key)
            idx2key.append((i, y))
        
        r = R % len(idx2key)
        
        for x in range(i, n):
            idx = key2idx[(x, i)]
            nidx = (idx+r) % len(idx2key)
            nx, ny = idx2key[nidx]
            arr[nx][ny] = A[x][i]

            idx = key2idx[(x, m-1)]
            nidx = (idx+r) % len(idx2key)
            nx, ny = idx2key[nidx]
            arr[nx][ny] = A[x][m-1]
        
        for y in range(i, m):
            idx = key2idx[(i, y)]
            nidx = (idx+r) % len(idx2key)
            nx, ny = idx2key[nidx]
            arr[nx][ny] = A[i][y]

            idx = key2idx[(n-1, y)]
            nidx = (idx+r) % len(idx2key)
            nx, ny = idx2key[nidx]
            arr[nx][ny] = A[n-1][y]
        
    return arr

if __name__ == '__main__':
    # 배열의 크기 N, M (2 <= N, M <= 300), 회전의 수 R (1 <= R <= 1e9)
    # min(N, M) % 2 == 0 --> N, M 중 작은 숫자는 무조건 짝수가 보장됨
    N, M, R = map(int, input().strip().split())
    for i in solve(N, M, R):
        print(*i)


"""
입력으로 주어진 비열을 R번 회전시킨 결과를 출력

크기가 N x M 인 배열이 있을 때, 배열을 반시계 방향으로 돌린다

min(N, M) mod 2 = 0 -> N, M 둘 중 작은 숫자는 무조건 짝수

첫번째 범위는 x = [0, N-1], y = [0, M-1]
두번째 범위는 x = [1, N-2], y = [1, M-2]

N, M 중 더 작은 값을 찾아야 함

껍질을 한줄로 펴서 위치를 구하는 느낌
"""