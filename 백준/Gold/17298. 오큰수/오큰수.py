import sys
input = sys.stdin.readline

# 각 원소 A[i]에 대해 오큰수 NGE(i)를 구해라
# A[i]의 오큰수는 오른쪽에 있으면서 A[i] 보다 큰 수 중 가장 왼쪽에 있는 수
# 없으면 -1

# 수열 A의 크기 N (1 <= N <= 1,000,000)

N = int(input().strip())

# 수열 A의 원소 A[i] (1 <= A[i] <= 1,000,000)
A = list(map(int, input().strip().split()))

# 수열 A가 주어졌을 때 i 위치에서의 A[i] 보다 큰 수를 찾아야 함
# 마지막 N 위치의 값은 -1

# 1. 오큰수는 i+1 이상 위치의 오른쪽의 숫자들 중 i와 가까운 위치에서 i보다 커야함
# - i < i+k and A[i] < A[i+k]

ans = [0]*N
stack = []
for i in range(N-1, -1, -1):
    while stack:
        if A[i] < stack[-1]: break
        stack.pop()
    
    if stack:
        ans[i] = stack[-1]
    else:
        ans[i] = -1
    
    stack.append(A[i])

print(*ans)

