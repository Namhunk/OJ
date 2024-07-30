import sys
input = sys.stdin.readline

# M개의 줄에 걸쳐 홍준이의 질문에 대한 명우의 답을 입력으로 주어진 순서에 따라서 출력, 펠린드롬인 경우 1, 아니면 0

N = int(input().strip()) # 수열의 크기 N (1 <= N <= 2,000)
arr = list(map(int, input().strip().split()))# 칠판에 적은 N개의 수

P = [[0]*N for _ in range(N)]
for i in range(N): # 1자리 숫자 팰린드롬 확인
    P[i][i] = 1

for i in range(N-1): # 길이 2의 팰린드롬 검사
    if arr[i] == arr[i+1]:
        P[i][i+1] = 1

for l in range(3, N+1): # 3 ~ N까지 검사
    for s in range(N-l+1):
        e = s+l-1
        if arr[s] == arr[e] and P[s+1][e-1]: # 양끝의 두 숫자가 일치하고, 사이의 수열이 팰린드롬이면
            P[s][e] = 1 # 그 수열도 팰린드롬

M = int(input().strip())
for _ in range(M):
    S, E = map(int, input().strip().split())
    print(P[S-1][E-1])