import sys

# A와 B의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기 K를 출력
# K != 0이라면 다음 줄에 K개의 수를 공백으로 구분해 출력
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().strip().split()))

num = 100 # 최대 100
AI, BI = 0, 0
ans = []

while num > 0:
    AL = A[AI:]
    BL = B[BI:]
    if num in AL and num in BL:
        ans.append(num)
        AI = AL.index(num)+AI+1
        BI = BL.index(num)+BI+1
    else:
        num -= 1

print(len(ans))
print(*ans)