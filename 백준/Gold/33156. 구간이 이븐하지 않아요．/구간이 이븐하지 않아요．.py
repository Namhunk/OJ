import sys
input = sys.stdin.readline


# 연속된 부분 수열 A[l,r]을 절반으로 나눠 얻은 두 수열이 서로 이븐할 때, A[l,r]의 최대 길이를 출력한다
# 만약 그러한 연속된 부분 수열이 존재하지 않는다면, 0을 출력한다

# 수열 A의 길이인 정수 N이 주어진다. (1 <= N <= 5,000)
N = int(input().strip())
A = list(map(int, input().strip().split()))

def solve(N, A):
    idx = {j: i for i, j in enumerate(sorted(set(A)))} # 각 숫자들을 크기순으로 0 부터 번호 부여
    D = len(set(A)) # 총 숫자들의 개수
    arr = [[0]*(N+1) for _ in range(D)] # 각 숫자들에 대해 중복되는 숫자의 위치를 나타낼 배열

    for i in range(N):
        arr[idx[A[i]]][i+1] = 1 # A 배열에서 현재 위치의 숫자에 1 표시

    for d in range(D):
        for i in range(1, N+1):
            arr[d][i] += arr[d][i-1] # 각 숫자들의 위치를 누적합으로 표시

    start = N if N % 2 == 0 else N-1 # 배열의 길이가 짝수인지 홀수인지에 따라 최대 길이 설정
    for i in range(start, 1, -2): # 길이는 짝수, 2씩 감소
        for l in range(N-i+1): # 시작점
            r = l + i - 1 # 종료 지점
            m = (l + r) // 2 # 중간
            flag = True # 배열의 숫자들이 같은지 확인

            for d in range(D): # 각 숫자들에 대해
                left = arr[d][m+1] - arr[d][l] # 왼쪽 배열
                right = arr[d][r+1] - arr[d][m+1] # 오른쪽 배열
                if left != right: # 왼쪽 오른쪽 배열에서 현재 숫자의 개수가 다른지
                    flag = False
                    break

            if flag: # 모든 숫자가 왼쪽 오른쪽에 같은 개수로 있다면
                return i

    return 0 # 없다면 0

print(solve(N, A))