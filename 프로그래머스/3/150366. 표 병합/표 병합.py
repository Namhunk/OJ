from collections import defaultdict

def init():
    global n, parent, members, arr, value_roots, answer
    n = 50
    parent = [[(i, j) for j in range(n+1)] for i in range(n+1)]
    members = {(i, j): {(i, j)} for i in range(1, n+1) for j in range(1, n+1)}
    arr = [[None]*(n+1) for _ in range(n+1)]
    value_roots = defaultdict(set)   # value -> {루트 좌표들}
    answer = []

def find(x, y):
    return parent[x][y]

def set_value(root, value):
    rx, ry = root
    old = arr[rx][ry]
    if old is not None:
        value_roots[old].discard(root)
    arr[rx][ry] = value
    if value is not None:
        value_roots[value].add(root)

def union(a, b, value):
    if a == b:
        set_value(a, value)
        return a
    if len(members[a]) < len(members[b]):
        a, b = b, a
    # 작은 집합 b를 큰 집합 a로 흡수 (small-to-large)
    for (x, y) in members[b]:
        parent[x][y] = a
    members[a] |= members[b]
    old_bv = arr[b[0]][b[1]]
    if old_bv is not None:
        value_roots[old_bv].discard(b)
    del members[b]
    set_value(a, value)
    return a

def UPDATE(cmd):
    if len(cmd) == 4:
        x, y, value = cmd[1:]
        root = find(int(x), int(y))
        set_value(root, value)
    else:
        v1, v2 = cmd[1:]
        for root in list(value_roots.get(v1, ())):
            set_value(root, v2)

def MERGE(cmd):
    x1, y1, x2, y2 = map(int, cmd[1:])
    a, b = find(x1, y1), find(x2, y2)
    va, vb = arr[a[0]][a[1]], arr[b[0]][b[1]]
    value = va if va is not None else vb
    union(a, b, value)

def UNMERGE(cmd):
    x, y = map(int, cmd[1:])
    root = find(x, y)
    value = arr[root[0]][root[1]]
    group = members[root]
    if value is not None:
        value_roots[value].discard(root)
    for (i, j) in group:
        parent[i][j] = (i, j)
        members[(i, j)] = {(i, j)}
        arr[i][j] = None
    arr[x][y] = value                # 선택한 셀만 원래 값 복원
    if value is not None:
        value_roots[value].add((x, y))

def PRINT(cmd):
    x, y = map(int, cmd[1:])
    root = find(x, y)
    v = arr[root[0]][root[1]]
    return v if v is not None else "EMPTY"

def solution(commands):
    init()
    answer = []
    for cmd in commands:
        cmd = list(cmd.split())
        if cmd[0] == 'UPDATE':
            UPDATE(cmd)
        
        elif cmd[0] == 'MERGE':
            MERGE(cmd)
        
        elif cmd[0] == 'UNMERGE':
            UNMERGE(cmd)
        
        else:
            answer.append(PRINT(cmd))

    
    return answer

'''
UPDATE r c value -> (r, c) 위치 셀 선택 -> 값을 value로 변경
UPDATE value1 value2 -> value1을 값으로 가진 모든 셀을 value2로 변경
MERGE r1 c1 r2 c2 -> (r1, c1) & (r2, c2) 두 셀을 합침, 값을 가진 셀이 있다면 둘다 그 값, 둘다 있다면 r1 c1
UNMERGE r c -> r c 셀의 병합을 해제 -> 선택된 셀이 포함한 모든 셀을 초기상태로 -> 이전값
PRINT r c -> (r, c) 위치의 셀을 선택하여 출력, 빈 경우 EMPTY 출력

-----------------------------------------------------------------------------------------
union-find 사용?
''' 