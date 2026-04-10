import sys
input = sys.stdin.readline

def solve(N):
    global Nodes, Cnt, Child, ans
    Nodes = [[] for _ in range(N+1)] # 각 노드의 자식 목록
    Cnt = [[0, 0] for _ in range(N+1)] # 각 노드의 구슬 개수 (하위 노드 포함, 자신만)
    Child = [0]*(N+1) # 각 노드의 자식의 수
    has_parent = [False]*(N+1)
    for _ in range(N):
        row = list(map(int, input().strip().split()))

        v = row[0] # 현재 노드
        Cnt[v][1] = row[1] # 개수 입력
        d = row[2] # 자식의 수

        for i in range(3, d+3):
            Nodes[v].append(row[i]) # 자식 입력
            has_parent[row[i]] = True
    
    # root를 탐색
    root = 1
    for i in range(1, N+1):
        if not has_parent[i]:
            root = i
            break

    ans = 0 # 정답
    function1(root)
    function2(root, 0)
    print(ans)

def function1(x): # 현재 자신의 구슬 개수가 자식의 개수보다 많다면 위로 보내줌
    global Child, Cnt, ans

    Child_cnt = 1 # 자식의 수 (자기자신 포함)
    for nx in Nodes[x]:
        cc, rc = function1(nx)

        Child_cnt += cc # 하위 자식의 수를 더해줌
        Cnt[x][1] += rc
        Cnt[x][0] += Cnt[nx][0]
    
    Child[x] = Child_cnt # 자식의 수 저장

    sub_total = Cnt[x][0] + Cnt[x][1] # 전체 개수
    ret_cnt = 0
    if sub_total > Child[x]: # 현재 구슬의 개수가 자식의 개수보다 많다면
        ret_cnt = sub_total - Child[x]
        Cnt[x][1] -= ret_cnt
        ans += ret_cnt

    Cnt[x][0] = sub_total - ret_cnt
    return Child[x], ret_cnt

def function2(x, y): # 상위 노드부터 남는 개수의 구슬을 자식에게 전해줌 x = 위치, y = 추가 구슬
    global ans, Cnt
    Cnt[x][0] += y
    Cnt[x][1] += y
    for nx in Nodes[x]:
        k = Child[nx] - Cnt[nx][0]
        if k > 0: # 하위 자식의 개수 > 하위 구슬의 개수 라면
            ans += k # 현재 구슬에서 필요한 만큼 가져감
            Cnt[x][1] -= k
            function2(nx, k)
        else:
            function2(nx, 0)

if __name__ == '__main__':
    while 1:
        # N (1 <= N <= 10,000)
        N = int(input().strip())
        if N <= 0: break

        solve(N)



"""
N개의 박스가 있다

각 정점은 1부터 n까지 번호가 있다 (1 <= n <= 10,000)

박스는 구슬을 몇개 포함하거나 비어있음 구슬의 총 개수 n개

모든 박스의 구슬 개수를 1로 만드려 함
이때 한 박스에 있는 구슬 하나를 인접한 박스로 옮기는 것이 한 번 움직이는 것

총 몇번을 움직여야 모든 구슬의 개수가 1개가 되는지

각 층에서 이웃한 노드에 구슬을 주기 위해서는 부모를 거쳐야 함

예제 1의 경우

1
│
│───┐───┐
2   3   4 
    │   │
    │─┐ │─┐─┐
    5 6 7 8 9

의 구조를 가짐
각 노드마다

1
│
│───┐───┐
1   1   1 
    │   │
    │─┐ │─┐─┐
    1 1 1 1 1

의 개수를 가짐

1-1. 자식이 없는 노드들 부터 자신의 개수를 제외한 나머지를 부모로 반환
    이때는 구슬의 개수가 이동의 횟수

1-2. 자식이 있는 부모는 자식의 개수 + 1 개를 남기고 부모로 보냄 (부족하다면 보내지 않음)

1-3. 결국 루트 노드에 도착함 

2-1. 현재 노드에서 다음 노드들 중 어떤 노드에 구슬을 보낼지 결정
    하위 자식의 수 = A, 해당 구역의 구슬 수 = B
    A > B 인 경우에 대해 현재 구슬을 이동시킴

    
3
2 0 1 3
3 2 1 1
1 1 0
0

2
│
3
│
1

0
│
2
│
1

"""