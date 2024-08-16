import sys
input = sys.stdin.readline

# K줄에 걸쳐서 수를 출력한다 i번쨰 줄에는 민수가 i번째로 낼 카드의 번호가 출력되어야 한다

# 세 개의 자연수 N, M, K (1 <= M <= N <= 4,000,000, 1 <= K <= min(M, 10,000))
N, M, K = map(int, input().strip().split())

# 카드의 번호를 나타내는 M개의 자연수 각 수들은 1 이상 N 이하이며 서로 다르다
card = [0]*(N+1) # N 개의 카드
for i in map(int, input().strip().split()): # 뽑은 카드 입력
    card[i] = i

before = 0
tmp = 0

for i in range(N, -1, -1):
    if card[i]: # 해당 번호의 카드가 있다면
        tmp = i-1

    card[i] = before # 이전 위치
    before = tmp

updates = []
# K개의 자연수, i번째 수는 철수가 i번쨰로 내는 카드의 번호이다. 철수가 내는 카드 역시 1 이상 N이하 이다
for i in map(int, input().strip().split()):
    while i != card[i]:
        updates.append(i)
        i = card[i]
    updates.append(i)
    i += 1
    print(i)
    for j in updates:
        card[j] = i
    updates.clear()



# N개의 빨강, 파랑 카드가 있고 각각 M개의 카드를 선택
# 철수는 빨간색, 민수는 파란색 카드를 갖는다
# 이 두명은 M개의 카드 중 1개를 선택, 그리고 두 카드의 숫자 비교를 K번 반복, 카드는 한 번만 사용 가능
# K번 동안 철수가 낼 카드를 알고 있을 때 철수가 낼 카드보다 큰 카드들 중 가장 작은 카드를 낸다

# refer to https://www.acmicpc.net/source/69414123