import sys
input = sys.stdin.readline

# 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력

# 트리의 노드의 개수 N (1 <= N <= 50)
N = int(input().strip())

# 각 노드의 부모, 부모가 없다면 -1
parents = list(map(int, input().strip().split()))

edges = [[] for _ in range(N)]
root = 0
for i in range(N):
    p = parents[i] # 부모 노드 위치
    if p == -1: # 루트인 경우 루트 노드 저장
        root = i
        continue
    edges[p].append(i)

D = int(input().strip()) # 삭제할 노드
def solve(idx):
    cnt = 0
    for nidx in edges[idx]:
        if D == nidx: continue
        cnt += solve(nidx)

    return cnt if cnt else 1

if D == root:
    print(0)
else:
    print(solve(root))


"""
"""