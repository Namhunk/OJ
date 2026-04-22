import sys
sys.setrecursionlimit(10**6)
# 1 <= len(nodeinfo) <= 10,000
def solution(nodeinfo):
    global answer
    arr = sorted([(x, y, i+1) for i, (x, y) in enumerate(nodeinfo)])
    answer = [[], []] # answer[0]: 전위, answer[1]: 후위
    
    find(arr)
    
    return answer

def find(arr):
    if arr:
        root = (0, -1, 0) # idx, y, 노드 번호 
        for i, (x, y, n) in enumerate(arr):
            if y > root[1]:
                root = (i, y, n)
        
        answer[0].append(root[-1])
        left, right = arr[:root[0]], arr[root[0]+1:]
        find(left), find(right)
        answer[1].append(root[-1])
        
            
            
"""
게임은 
두 팀이 있을때, 각 팀이 같은 곳을 다른 순서로 방문하도록 해서
먼저 순회를 마친 팀이 승리

트리를 구성하는 모든 노드의 x, y 좌표는 정수
모든 노드는 서로 다른 x를 가짐
같은 레벨에 있는 노드는 같은 y를 가짐
자식 노드의 y는 항상 부모 노드보다 작다
임의의  노드 V의 왼쪽 서브트리에 있는 모든 노드의 x값은 V의 x값 보다 작다
임의의 노드 V의 오른쪽 서브 트리에 있는 모든 노드의 x값은 V의 x값 보다 크다

노드의 이진트리를 전위, 후위 순회한 결과를 2차원 배열에 담아 return

1. 노드는 1 ~ N까지의 정수

1   [5, 3]
2   [11, 5]
3   [13, 3]
4   [3, 5]
5   [6, 1]
6   [1, 3]
7   [8, 6]
8   [7, 2]
9   [2, 2]

1. 현재 y위치의 x를 기준으로 left, right로 분리
2. 


[(6, 1, 3), (9, 2, 2), (4, 3, 5), (1, 5, 3), (5, 6, 1), (8, 7, 2), (7, 8, 6), (2, 11, 5), (3, 13, 3)]

[(6, 1, 3), (9, 2, 2), (4, 3, 5), (1, 5, 3), (5, 6, 1), (8, 7, 2)] [ (2, 11, 5), (3, 13, 3)]

[(6, 1, 3), (9, 2, 2)] [(1, 5, 3), (5, 6, 1), (8, 7, 2)] [(3, 13, 3)]

[(9, 2, 2)] [(5, 6, 1), (8, 7, 2)]

[(5, 6, 1)]

[]
"""