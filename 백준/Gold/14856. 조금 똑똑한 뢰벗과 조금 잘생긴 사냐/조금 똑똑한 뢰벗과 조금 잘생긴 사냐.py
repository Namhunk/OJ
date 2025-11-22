import sys
input = sys.stdin.readline

# N < 10**18
N = int(input().strip())

# 자연수를 연속하지 않은 피보나치 수의 합으로 나타내라
# 첫째 줄에 k값
# 둘째 줄에 F(i1), F(i2), ... F(ik)
# 없다면 -1
# 연속하지 않은 수들을 구하려면 N값 보다 작고 가장 가까운 피보나치 수를 뺴야 함

F = [0, 1] # 피보나치 계산 저장

i = 1
while F[-1] < N:
    F.append(F[i] + F[i-1])
    i += 1

ans = []
for i in range(len(F)-1, 1,  -1):
    if F[i] <= N:
        N = N - F[i]
        ans.append(F[i])


print(len(ans))
print(*ans[::-1])