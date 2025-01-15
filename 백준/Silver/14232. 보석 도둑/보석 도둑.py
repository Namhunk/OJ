import sys
from math import sqrt, ceil
input = sys.stdin.readline

# 첫째 줄은 효빈이가 훔쳐올 보석의 개수, 다음 줄은 훔쳐올 보석의 무게를 오름차순 출력

# 효빈이가 들 수 있는 무게 k ( 2 <= k <= 10^12)
k = int(input().strip())

ans = []
for i in range(2, ceil(sqrt(k))+1):
    while k % i == 0:
        ans.append(i)
        k //= i

if k != 1:
    ans.append(k)

print(len(ans))
print(*ans)