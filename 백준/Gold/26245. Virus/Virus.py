import sys
input = sys.stdin.readline

"""
전체 arr는 n x m
1. 스폰지밥은 학교에 가기 싫어서 아플 예정
2. n x m의 배열에서 기준점 arr[n][m] = 0 일때 상하좌우 이웃한 위치에 1이 2개 존재할 경우 감염
3. 1을 최소로 갖고 모든 세포를 감염시킬 수 있는 배열 생성
"""
# n, m (1 <= n, m <= 1e3)
n, m = map(int, input().strip().split())

MIN = min(n, m) # 처음 작은 사각형은 대각선으로 1을 만들어줌
MAX = max(n, m)
arr = [['0']*m for _ in range(n)]

# 0, 0 부터 대각선을 모두 1로 변경
for i in range(MIN):
    arr[i][i] = '1'

# 직사각형인 경우 나머지 채워줌
for i in range(MIN-1, MAX, 2):
    if n < m:
        arr[MIN-1][i] = '1'
    elif n > m:
        arr[i][MIN-1] = '1'

# 마지막 arr[-1][-1]위치가 1인지 확인 후 변경
arr[-1][-1] = '1'

for i in arr:
    print(''.join(i))

"""
n, m 둘 중 최소로 갖는 값을 k(k = min(n, m))라고 할 때 시작점 0, 0부터 k x k 의 크기만큼 대각성분들을
1로 바꿔주면 k x k는 무조건 모두 1로 감염됨
그리고 1값을 갖는 초기 셀의 개수 c는 c = (n + m) / 2)일때 가장 최소의 개수를 갖음
n = 5, m = 9 라고 하면 c = 7개 나머지 2개는 가장 하단에 징검다리 식으로 추가하면 됨
"""