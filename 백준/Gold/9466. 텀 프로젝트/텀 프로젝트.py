import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다(단, 단 한 명만 선택 가능)
# 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능

# 각 테스트 케이스마다 프로젝트 팀에 속하지 못한 학생들의 수를 나타내라

def dfs(x):
    global cnt
    visit[x] = False
    y = arr[x]
    if visit[y]:
        dfs(y)
    else:
        if y not in team:
            z = y
            while z != x:
                cnt += 1
                z = arr[z]

            cnt += 1

    team.add(x)

# 테스트 케이스의 개수 T
T = int(input().strip())
for _ in range(T):
    # 학생의 수 n (2 <= n <= 100,000)
    n = int(input().strip())
    # 1 ~ n 까지의 각 학생들이 같은 팀이 되길 희망하는 학생들의 번호
    arr = [0] + list(map(int, input().strip().split()))
    visit = [True]*(n+1)
    cnt = 0
    team = set()
    for i in range(1, n+1):
        if visit[i]:
            dfs(i)
    print(n - cnt)
