import sys
input = sys.stdin.readline

# 첫째 줄에 비내림차순으로 만드는 수열 P를 출력

# 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같은 경우
# 배열 A의 크기 N(1 <= N <= 50)
N = int(input().strip())

# 배열 A의 원소 (1 <= A[i] <= 1,000)
A = list(map(int, input().strip().split()))

# B[P[i]] = A[i]

num = {i: [] for i in range(1, 1001)} # 각 숫자에 대한 위치 번호

for i, j in enumerate(sorted(A)): # 배열 A를 정렬해서 위치 추가
    num[j].append(i)

idx = [0]*(1001) # 각 숫자의 몇번쨰 숫자를 사용하는지
ans = []
for i in range(N):
    ans.append(num[A[i]][idx[A[i]]])
    idx[A[i]] += 1

print(*ans)