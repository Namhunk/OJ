import sys
input = sys.stdin.readline

    
def solve(V, E, G, deg):
    odd = [i for i in range(V+1) if deg[i] % 2]
    if len(odd) not in (0, 2): # 홀수 차수 정점이 0개 또는 2개가 아니라면
        return "NO"

    start = odd[0] if odd else next((i for i in range(V+1) if deg[i] > 0), 0)

    used = [False]*E
    stack, path = [start], []
    while stack:
        u = stack[-1]
        while G[u] and used[G[u][-1][1]]:
            G[u].pop()

        if G[u]:
            v, i = G[u].pop()
            used[i] = True
            stack.append(v)
        else:
            path.append(stack.pop())

    return "YES" if len(path) == E+1 else "NO"

def main():
    # V, E (1 <= V <= E <= 3000)
    V, E = map(int, input().strip().split())

    G = [[] for _ in range(V+1)]
    deg = [0]*(V+1)


    for i in range(E):
        a, b = map(int, input().strip().split())
        G[a].append((b, i))
        G[b].append((a, i))
        deg[a] += 1
        deg[b] += 1

    print(solve(V, E, G, deg))

if __name__ == '__main__':
    main()
"""
퍼레이드 경로는 일정한 지점들과 두 지점을 연결하는 구간
*모든 지점을 지나면서 모든 연결구간들을 지나고 싶어한다*

원하는 노선을 만들 수 있다면 YES, 없다면 NO

X - Y 이동은 한번만 가능
----------------------------------------
모든 연결 구간, 모든 지점을 지나는 경로를 구할 수 있는가?

오일러 경로 : 차수가 홀수인 정점이 정확히 0개 또는 2개라면 그 중 하나에서 출발해 다른 하나에서 끝남

"""