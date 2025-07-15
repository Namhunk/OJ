import sys
input = sys.stdin.readline

# 좋은 수 는 총 몇개인가?; 좋은 수 란 A[i]가 A[0 ~ i-1]의 숫자 세 개의 합으로 나타낼 수 있어야 함

# N (1 <= N <= 5,000)
N = int(input().strip())

# A (-100,000 <= A[i] <= 100,000)
A = list(map(int, input().strip().split()))

size = 10**5*2 # |-10**5 or 10**5| 크기
Two = [0]*(size*2+1) # 범위의 길이, 두 수의 합을 저장

ans = 0
for i in range(N):
    for j in range(i):
        if Two[A[i]-A[j]+size]:
            ans += 1
            break

    for j in range(i+1):
        Two[A[i]+A[j]+size] = 1

print(ans)



"""


"""