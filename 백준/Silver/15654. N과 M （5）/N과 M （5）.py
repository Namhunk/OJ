import sys

# 자연수 N, M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열을 모두 출력
# N개의 자연수 중에서 M개를 고른 수열

# 수열을 담거나, 출력하는 함수
def print_seq(sequence):
    global visit
    # 현재 수열의 길이가 M과 같다면 수열 출력
    if len(sequence) == M: return print(*sequence)
    # 아니면
    else:
        for i in range(len(arr)):
            # 방문하지 않았다면
            if visit[i]:
                # 방문처리 후
                visit[i] = 0
                # 수열에 담고 함수 실행
                print_seq([*sequence, arr[i]])
                # 방문처리 해제
                visit[i] = 1

# N, M 입력
N, M = map(int, sys.stdin.readline().strip().split())
# 배열 입력과 동시에 배열안의 숫자들 정렬
arr = sorted(list(map(int, sys.stdin.readline().strip().split())))
# 방문 배열 생성
visit = [1]*len(arr)

# 가장 처음에 오는 숫자를 고르는 반복문
for i in range(len(arr)):
    # 만약 방문하지 않았다면
    if visit[i]:
        # 방문처리 후
        visit[i] = 0
        # 함수 실행
        print_seq([arr[i]])
        # 방문처리 해제
        visit[i] = 1