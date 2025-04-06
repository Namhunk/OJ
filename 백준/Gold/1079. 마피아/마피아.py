import sys
input = sys.stdin.readline

# 최적의 선택을 할 때, 몇 번의 밤이 지나는지 출력

# 참가자의 수
N = int(input().strip())

# 각 참가자의 유죄 지수
guilty = list(map(int, input().strip().split()))

# 배열 R
R = [list(map(int, input().strip().split())) for _ in range(N)]

# 은진이의 참가자 번호
E = int(input().strip())

cnt = N # 생존자 수
survivors = [True]*N # 각 생존 표시

# 낮, 밤 이 한 세트

def vote(guilty): # 투표
    MaxGuilty = -float('inf')
    idx = 0

    for i in range(N):
        if not survivors[i]:
            continue

        if MaxGuilty < guilty[i]:
            MaxGuilty = guilty[i]
            idx = i

    survivors[idx] = False

    return idx

def kill(guilty, i):
    survivors[i] = False
    for j in range(N):
        if i == j:
            continue

        guilty[j] += R[i][j]

def dfs(cnt, tmp):
    global ans
    ans = max(ans, tmp)
    if (cnt == 1 and survivors[E]) or (not survivors[E]): # 마피아만 살거나 마피아가 죽었다면
        return

    if cnt % 2:
        idx = vote(guilty)
        dfs(cnt-1, tmp)
        survivors[idx] = True
        return

    for i in range(N):
        if not survivors[i] or i == E: continue

        kill(guilty, i)
        dfs(cnt-1, tmp+1)
        survivors[i] = True
        for j in range(N):
            if i == j:
                continue

            guilty[j] -= R[i][j]

ans = 0
dfs(N, 0)
print(ans)
"""
1. 참가자는 마피아, 시민 그룹으로 나뉘어짐, 시민들은 마피아의 정체를 모름 참가자는 0번부터
2. 참가자가 짝수 명 남으면 밤, 밤에는 마피아가 죽일 사람 한 명을 고르고 죽임
3. 참가자 홀수 명 남으면 낮, 낮에는 투표
4. 마피아 0명 or 시민 0명은 게임 종료

유죄 지수는 낮에 시민들이 어떤 참가자를 죽일 것인지 고를 때 쓰임
R은 참가자의 반응

1. 밤에는 마피아가 죽일 사람을 한 명 고른다. 이 경우 각 사람의 유죄 지수가 바뀐다. 만약 참가자 i가 죽었다면, 다른 참가자 j의 유죄 지수는 R[i][j]만큼 변한다.
2. 낮에는 현재 게임에 남아있는 사람 중에 유죄 지수가 가장 높은 사람을 죽인다. 그런 사람이 여러 명일 경우 그중 번호가 가장 작은 사람이 죽는다. 이 경우 유죄 지수는 바뀌지 않는다.
"""