import sys
input = sys.stdin.readline

# 배열의 합의 최대값을 출력

# 배열에서 두 원소 A[i], A[j]를 선택 (i != j)
# 선택한 두 원소를 모두 A[i] x A[j]로 바꿈
# 이 연산은 최대 1번

# 배열의 크기 N (2 <= N <= 2 x 10^5)
N = int(input().strip())

# 배열의 원소인 N개의 정수 (-10^9 <= A[i] <= 10^9)
arr = sorted(list(map(int, input().strip().split())))

ans1 = sum(arr)
ans2 = max(ans1, ans1 + (arr[0] * arr[1] * 2) - (arr[0]+arr[1]))
ans3 = max(ans1, ans1 + (arr[N-1] * arr[N-2] * 2) - (arr[N-1]+arr[N-2]))

print(max(ans1, ans2, ans3))
"""
배열을 정렬했을때
1. 가장 작은 두 정수의 곱의 합이 크다
2. 가장 큰 두 정수의 곱의 합이 크다
3. 그냥 더하는게 크다
"""