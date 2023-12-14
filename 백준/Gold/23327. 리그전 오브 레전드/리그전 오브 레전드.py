import sys

n, q = map(int, sys.stdin.readline().strip().split())

arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
sum_arr = arr.copy()
pow_arr = [0]*len(arr)

for i in range(1, n+1):
    sum_arr[i] += sum_arr[i-1]
    pow_arr[i] = arr[i]**2 + pow_arr[i-1]

for _ in range(q):
    # idx - l <= i <= r 의 팀들이 참가 
    l, r = map(int, sys.stdin.readline().strip().split())

    print(((sum_arr[r] - sum_arr[l-1])**2 - (pow_arr[r] - pow_arr[l-1]))//2)

"""
1   2   3
x   y   z

ans = (x*y) + (x*z) + (y*z) = (x*y) + (y*z) + (z*x)
= x*y + y*z + z*x

= (x+y+z)^2 = x^2 + y^2 + z^2 + 2(x*y + y*z + z*x)
== ((x+y+z)^2 - (x^2 + y^2 + z^2)) // 2 = ans
"""