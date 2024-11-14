import sys
input = sys.stdin.readline

# 개미굴의 시각화 된 구조를 출력, 각 층은 "--"로 구분하며, 사전 순

# 로봇 개미가 각 층을 따라 내려오면서 알게 된 먹이의 정보 개수 N(1 <= N <= 1000)
N = int(input().strip())
food = []
for _ in range(N):
    # 시작은 로봇 개미 한마리가 보내준 먹이 정보 개수 K(1 <= K <= 15)
    # 다음 K개의 입력은 로봇 개미가 왼쪽부터 순서대로 각 층마다 지나온 방에 있는 먹이 정보
    food.append(list(input().strip().split())[1:])

# 정렬 후 중복 되지 않는 값만 출력
food.sort()
dash = '--'
for i in range(N):
    if i == 0:
        for j in range(len(food[i])):
            print(j*dash+food[i][j])
    else:
        start = 0
        for j in range(len(food[i])):
            if food[i-1][j] != food[i][j]:
                start = j
                break

        for j in range(start, len(food[i])):
            print(j*dash+food[i][j])
