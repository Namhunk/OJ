import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 현재 동맹인 왕국을 찾음
def find(x):
    if parents[x] != x: # 부모의 왕국과 동맹인 왕국을 찾음
        parents[x] = find(parents[x])
    
    return parents[x]

# 왕국간의 동맹
def union(x, y):
    x, y = find(x), find(y)

    # 숫자가 작은 왕국을 부모로
    if x < y: x, y = y, x

    parents[x] = parents[y]


def solve():
    global parents
    # 왕국의 수 N (1<= N <= 100,000), 동맹 관계의 수 M (1 <= M <= 200,000)
    N, M = map(int, input().strip().split())

    # 각 왕국의 동맹 상태
    parents = [i for i in range(N+1)]

    # M개의 줄에 X, Y 입력 (X, Y 왕국들이 동맹이다)
    for _ in range(M):
        X, Y = map(int, input().strip().split())
        union(X, Y) # 동맹 실행

    # CTP 왕국의 번호 C, 한솔 왕국의 번호 H, 추가 동맹의 기회 K (0 <= K <= 100)
    C, H, K = map(int, input().strip().split())

    C_parent = find(C) # C의 부모 왕국을 찾음
    H_parent = find(H) # H의 부모 왕국을 찾음
    ans = 0

    force = {} # 각 동맹들간의 부모: 힘을 나타냄
    for i in range(1, N+1):
        idx = find(parents[i]) # 부모 왕국의 번호

        if H_parent == idx: continue # 한솔 왕국 동맹의 부모 번호라면 넘어감
        if C_parent == idx: # CTP 왕국과 이미 동맹이라면 정답에 +1
            ans += 1
            continue

        force[idx] = force.get(idx, 0) + 1
    
    # 힘의 크기대로 정렬(크기 내림차순)
    sorted_force = sorted([v for k, v in force.items()], reverse=True)

    # 배열의 길이와 K값 중 더 작은 크기로 반복문 수행
    for i in range(min(len(sorted_force), K)):
        ans = ans + sorted_force[i]

    return ans

if __name__ == '__main__':
    print(solve())



"""
CTP 왕국의 힘의 최댓값 출력

- 동맹이 없는 나라의 힘은 1
- A, B가 동맹이고 B, C가 동맹이면 A, C가 동맹이다
- CTP 왕국은 최대 K번 다른 왕국과 동맹을 맺을 기회를 갖는다.
- CTP 왕국, 한솔 왕국은 서로 동맹을 맺을 수 없으며, 한솔 왕국과 동맹인 왕국과도 동맹을 맺을 수 없음

"""