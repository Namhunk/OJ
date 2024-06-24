import sys

N = int(sys.stdin.readline().strip())
S = list(map(int, sys.stdin.readline().strip().split()))

# 가장 앞, 뒤의 과일을 제거하면서 두 종류 이하의 과일만을 남게 했을때의 탕후루의 최대 길이
# 과일 종류는 1 ~ 9 

ans, cnt = 0, 0
l, r = 0, 0

fruit = [0]*10

while r < N:
    if not fruit[S[r]]: cnt += 1
    
    fruit[S[r]] += 1
    r += 1

    if cnt > 2:
        while l < r:
            fruit[S[l]] -= 1
            if not fruit[S[l]]: break
            l += 1
        l += 1
        cnt -= 1
    ans = max(ans, r-l)

print(ans)