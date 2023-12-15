import sys

# 자연수 N, M이 주어졌을 때, 조건을 만족하는 길이가 M인 수열을 구해라
# N개의 자연수 중에서 M개를 고른 수열

# 중복되는 수열은 한번만 출력

# 수열 생성 및 출력 함수
def print_seq(sequence):
    global visit, printed
    
    # 수열의 길이가 M 과 같다면
    if len(sequence) == M:
        # 수열 배열을 문자열로 변환
        string = " ".join(sequence)
        # 문자열이 현재까지 출력되지 않았다면
        if string not in printed:
            # 출력 배열에 넣음
            printed.append(string)
            return
    else:
        for i in range(N):
            # 방문하지 않았다면
            if visit[i]:
                # 방문처리
                visit[i] = 0
                # 함수 실행
                print_seq([*sequence, arr[i]])
                # 방문 해제
                visit[i] = 1

# N, M 입력
N, M = map(int, sys.stdin.readline().strip().split())
# 배열 입력
arr = list(sys.stdin.readline().strip().split())
# 정렬
arr = sorted(arr, key= lambda x: int(x))
# 방문 배열
visit = [1]*N
# 출력 저장 배열
printed = []

for i in range(N):
    if visit[i]:
        visit[i] = 0
        print_seq([arr[i]])
        visit[i] = 1

for i in printed:
    print(i)