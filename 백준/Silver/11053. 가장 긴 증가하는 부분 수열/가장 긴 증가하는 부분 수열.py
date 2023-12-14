import sys

# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하기

# 수열 A의 크기 n
n = int(sys.stdin.readline().strip())

#  수열 A의 값
A = [0] + list(map(int, sys.stdin.readline().strip().split()))
Dict = {i: 0 for i in A}

ans = 0
for i in range(1, n+1):
    for j in range(i):
        if A[i] > A[j]:
            Dict[A[i]] = max(Dict[A[i]], Dict[A[j]]+1)
    
    ans = max(ans, Dict[A[i]])

print(ans)
"""
"""