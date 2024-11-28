import sys
input = sys.stdin.readline

# M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력한다
# 세그먼트 트리?
# 첫째 줄에 N, M이 주어진다.
N, M = map(int, input().strip().split())

# 다음 N개의 줄에는 N개의 정수가 주어진다.
arr = [int(input().strip()) for _ in range(N)]

MIN = [0]*(4*N) # 최솟값 트리
MAX = [0]*(4*N) # 최댓값 트리

def init(start, end, idx): # 트리 초기화
    if start == end:
        MIN[idx] = arr[start] # 최솟값 저장
        MAX[idx] = arr[start] # 최댓값 저장

    else:
        mid = (start + end) // 2
        init(start, mid, idx*2)
        init(mid+1, end, idx*2+1)

        MIN[idx] = min(MIN[idx*2], MIN[idx*2+1])
        MAX[idx] = max(MAX[idx*2], MAX[idx*2+1])

def find(start, end, idx, left, right): # 최솟값, 최댓값 구하는 함수
    if left > end or right < start: # 범위를 벗어나면
        return [float('inf'), 0]

    if left <= start and right >= end: # 범위가 아닌 위치라면
        return [MIN[idx], MAX[idx]]

    mid = (start + end) // 2
    # 왼쪽, 오른쪽 범위 각각의 최솟값, 최댓값
    ret1 = find(start, mid, idx*2, left, right)
    ret2 = find(mid+1, end, idx*2+1, left, right)

    return [min(ret1[0], ret2[0]), max(ret1[1], ret2[1])] # 최소끼리, 최대끼리

init(0, N-1, 1)
for _ in range(M):
    a, b = map(int, input().strip().split())
    print(*find(0, N-1, 1, a-1, b-1))
