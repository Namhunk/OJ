import sys, math

# 배열의 서로 다른 두 정수의 곱의 모든 합
n = int(sys.stdin.readline().strip())
arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
pow2_arr = [0] + [arr[i]**2 for i in range(1, n+1)]
for i in range(1, n + 1):
    pow2_arr[i] += pow2_arr[i-1]
    arr[i] += arr[i-1]

ans = (arr[n]**2 - pow2_arr[n])//2
print(ans)
"""

ab + bc + cd + ... + na = ans
(a + b + c + ... n)^ans = a^2 + b^2 + ... n^2 + 2*ans

"""