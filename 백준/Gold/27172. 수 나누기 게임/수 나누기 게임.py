import sys
input = sys.stdin.readline

# 첫 번째 플레이어부터 N번째 플레이어까지 게임이 종료됐을 때 각 플레이어의 점수를 공백으로 구분해 출력

# 수 나누기 게임 규칙
# 1. 게임을 시작하기 전 각 플레이어는 1 ~ 1,000,000 사이의 수가 적힌 서로 다른 카드를 잘 섞은 뒤 한 장씩 나눠 갖는다
# 2. 매 턴마다 플레이어는 다른 플레이어와 한 번씩 결투를 한다
# 3. 결투는 서로 카드를 보여주는 방식, 두 카드 중 약수 카드를 가진 쪽이 승리, 아니면 무승부
# 4. 승리자는 +1점, 패배자는 -1점, 무승부는 변화 없음
# 본인을 제외한 다른 모든 플레이어와 정확히 한 번씩 결투를 하면 게임이 종료

# 플레이어의 수 N(2 <= 100,000)
N = int(input().strip())

# 각 플레이어의 카드 숫자 X[i](1 <= X[i] <= 1,000,000)
# 1 <= i < j <= N 에 대해 X[i] != X[j] -> 각 카드는 중복되지 않는다
X = list(map(int, input().strip().split()))

MAX = int(1e6) # 최대 범위
visit = [False]*(MAX+1) # 존재하는 카드인지 표시
cnt = [0]*(MAX+1) # 정답 저장
for i in X:
    visit[i] = True

for i in range(1, MAX+1):
    if not visit[i]: continue # 숫자 i가 존재하는 카드인 경우

    for j in range(i*2, MAX+1, i):
        if not visit[j]: continue # 숫자 j가 존재하는 카드인 경우
        cnt[i] += 1
        cnt[j] -= 1

for i in X:
    print(cnt[i], end=' ')