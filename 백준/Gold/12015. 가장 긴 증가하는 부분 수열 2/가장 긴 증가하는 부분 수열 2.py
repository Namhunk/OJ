import sys
input = sys.stdin.readline

# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력
N = int(input().strip()) # 수열 A의 크기 N (1 <= N <= 1,000,000)
A = list(map(int, input().strip().split())) # 수열 A (1 <= A[i] <= 1,000,000)

seq = [A[0]] # 정답이 들어갈 배열
for i in range(1, N):
    if A[i] > seq[-1]: # 현재 숫자가 정답 배열의 마지막 값보다 크다면
        seq.append(A[i]) # A[i] 추가
    else: # 작거나 같다면
        l, r = 0, len(seq)-1 # 정답 배열의 범위 안에서
        while l < r:
            m = (l+r)//2

            if seq[m] < A[i]: l = m+1
            else: r = m

        seq[l] = A[i] # 현재 A[i]보다 작은 값으로 교체

print(len(seq))