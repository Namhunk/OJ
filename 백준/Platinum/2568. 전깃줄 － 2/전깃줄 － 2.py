import sys
input = sys.stdin.readline

# 첫째 줄에 두 전봇대 사이의 모든 전깃 줄이 서로 교차하지 않게 하기 위해 없애야 하는 전깃줄의 최소 개수 출력
# 둘째 줄부터 한 줄에 하나씩 없애야 하는 전깃줄의 A 전봇대에 연결되는 위치의 번호를 오름차순으로 출력
# 만약 답이 두 가지 이상이라면 그 중 하나를 출력

# 두 전봇대 사이의 전깃줄의 개수 N (1 <= N <= 100,000)
N = int(input().strip())
# 각 전깃줄이 전봇대 A, B가 연결되는 위치의 번호 500,000 이하의 자연수, 각 위치는 일대일 대응
cable = [list(map(int, input().strip().split())) for _ in range(N)]

# 전깃줄이 서로 교차하지 않으려면
# 위치의 번호들이 증가하는 수열의 형태를 이뤄야 함
# 가장 긴 증가하는 부분 수열 5와 비슷

# A 전봇대의 위치를 기준으로 정렬
A = sorted(cable)

# B 전봇대의 위치를 기준으로 정렬
B = sorted(cable, key=lambda x: x[1])

seqA = [A[0]] # A의 위치에 연결되는 B 위치의 번호
seqB = [B[0]] # B의 위치에 연결되는 A 위치의 번호

# 각 A, B 전봇대의 i 위치일때 연결 개수
cableA = [0]*N
cableB = [0]*N

cableA[0], cableB[0] = 1, 1

for i in range(1, N):
    if seqA[-1][1] < A[i][1]:
        seqA.append(A[i])
        cableA[i] = len(seqA)
    else:
        l, r = 0, len(seqA)
        while l < r:
            m = (l+r)//2
            if seqA[m][1] < A[i][1]: l=m+1
            else: r=m

        seqA[l] = A[i]
        cableA[i] = l+1

    if seqB[-1][0] < B[i][0]:
        seqB.append(B[i])
        cableB[i] = len(seqB)
    else:
        l, r = 0, len(seqB)-1
        while l < r:
            m = (l+r)//2
            if seqB[m][0] < B[i][0]: l=m+1
            else: r=m

        seqB[l] = B[i]
        cableB[i] = l+1

# 각 A, B에 대한 길이
cntA = len(seqA)
cntB = len(seqB)

ansA, ansB = [], []
for i in range(N-1, -1, -1):
    if cableA[i] == cntA: cntA -= 1
    else: ansA.append(A[i][0])

    if cableB[i] == cntB: cntB -= 1
    else: ansB.append(B[i][0])

if len(ansA) > len(ansB):
    print(len(ansA))
    print(*sorted(ansA), sep='\n')
else:
    print(len(ansB))
    print(*sorted(ansB), sep='\n')