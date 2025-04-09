import sys
input = sys.stdin.readline

# 정렬한 결과를 출력

# 배열의 크기 N (1 <= N <= 50)
N = int(input().strip())

# 배열 A
A = list(map(int, input().strip().split()))

# 교환 횟수 S (0 <= S <= 1,000,000)
S = int(input().strip())

# 횟수를 다 쓰기 전 앞에서 부터 가져올 수 있는 범위 내 최댓값을 가져와야 함
i = 0
while S > 0 and i < N:
    m = A.index(max(A[i:i+S+1])) # 앞으로 가져올 수 있는 위치 중 최대값 위치 탐색
    if m != i: # 두 위치가 다르면
        A[m], A[m-1] = A[m-1], A[m] # 교환
        S -= 1 # 횟수 1 차감
    else:
        i += 1

print(*A)