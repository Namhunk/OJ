# key = M x M (3 <= M <= 20)
# lock = N x N (3 <= N <= 20)
# M <= N
def solution(key, lock):
    global n, m
    answer = False
    n = len(lock)
    m = len(key)
    
    size = n + 2 * m
    MAP = [[0] * size for _ in range(size)]
    for i in range(n):
        for j in range(n):
            MAP[i + m][j + m] = lock[i][j]
            
    for _ in range(4):
        key = rotate(key)

        # key를 (dx, dy)만큼 이동시키는 모든 경우
        for dx in range(0, m + n):
            for dy in range(0, m + n):
                # 2-1. 현재 위치에 key를 더해보기
                for i in range(m):
                    for j in range(m):
                        MAP[i + dx][j + dy] += key[i][j]

                # 2-2. 실제 lock 영역(m ~ m+n-1, m ~ m+n-1)이 모두 1인지 체크
                if check_lock(MAP, n, m):
                    return True

                # 2-3. 다시 빼서 원상복구
                for i in range(m):
                    for j in range(m):
                        MAP[i + dx][j + dy] -= key[i][j]

    return False

def rotate(arr): # 회전은 시계방향 고정
    new_arr = []
    for j in range(m):
        row = []
        for i in range(m-1, -1, -1):
            row.append(arr[i][j])
        new_arr.append(row)
        
    return new_arr
            
def check_lock(MAP, n, m):
    # 중앙의 실제 자물쇠 영역이 모두 1인지 검사
    for i in range(n):
        for j in range(n):
            if MAP[i + m][j + m] != 1:
                return False
    return True
'''
열쇠로 자물쇠를 열 수 있으면 true, 열 수 없으면 false를 return

열쇠는 회전, 이동 가능

시작은 4가지 상태
각 회전 상태에 대해 이동 수행
---------------------------------------------------------
1. key 회전
2. 각 회전한 key 주변 상하좌우 각각 m길이의 0 추가
3. m x m 윈도우 중 Lock의 형태와 맞는지 확인


'''