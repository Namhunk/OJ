import sys

# 바이토닉 수열이란 수열에서 어떤 한 숫자를 기준으로
# 왼쪽, 오른쪽 방향으로 숫자들이 감소를 해야함.(기준 숫자가 처음, 마지막에 없는 경우)
# 만약 기준이 되는 숫자가 수열의 첫 위치 or 마지막 위치에 있다면
# 연속으로 감소 or 연속으로 증가 해야함

# 수열 A의 부분 수열 중에서 가장 긴 바이토닉 수열의 길이를 출력

# 수열 A의 크기 N 입력 (1 <= N <= 1000)
N = int(sys.stdin.readline().strip())

# 수열 A 입력
A = list(map(int, sys.stdin.readline().strip().split()))
B = A[::-1] # 수열 A의 역순

inc = [1]*N  # 증가
dec = [1]*N # 감소

# 수열을 돌면서 i 위치 일때 가장 긴 수열을 저장
for i in range(N):
    for j in range(i):
        if A[i] > A[j]: inc[i] = max(inc[i], inc[j] + 1)
        
        if B[i] > B[j]: dec[i] = max(dec[i], dec[j] + 1)

dec = dec[::-1] # 감소 배열을 증가 배열의 순서와 맞춤

ans = 0 # 정답 저장
for i in range(N):
    # i 위치에서 증가 + 감소의 - 1(자기 자신이 2번 포함되므로 1번 빼줌) 최대값
    ans = max(ans, inc[i] + dec[i] - 1)

print(ans)