from collections import deque
import sys

def union(a_row, a_col, b_row, b_col):
    origin_a = find(a_row, a_col)
    origin_b = find(b_row, b_col)

    if origin_b == origin_a: return 

    if origin_b not in origin_set:
        MAP[b_row][b_col] = origin_a
        return

    if origin_a not in origin_set:
        MAP[a_row][a_col] = origin_b
        return

    if origin_a < origin_b:
        MAP[b_row][b_col] = origin_a
        origin_set.remove(origin_b)
        origin_location[origin_b] = origin_location[origin_a]
        return

    else:
        MAP[a_row][a_col] = origin_b
        origin_set.remove(origin_a)
        origin_location[origin_a] = origin_location[origin_b]
        return


def find(row, col):
    x = MAP[row][col]

    if x in origin_set: return x

    x_row, x_col = origin_location[x]
    origin = find(x_row, x_col)
    MAP[row][col] = origin

    return origin


DX = (0, 0, -1, 1)
DY = (-1, 1, 0, 0)

N, K = map(int, sys.stdin.readline().strip().split())
MAP = [[0] * N for _ in range(N)]

origin_location = dict()
origin_set = set(range(1, K + 1))

civ_que = deque()
next_que = deque()

for civilization in range(1, K + 1):
    row, col = map(int, sys.stdin.readline().strip().split())
    row -= 1
    col -= 1

    MAP[row][col] = civilization
    origin_location[civilization] = (row, col)

    civ_que.append((row, col))

for civ in civ_que:
    row, col = civ

    for direction in range(4):
        next_row = row + DY[direction]
        next_col = col + DX[direction]

        if N > next_row >= 0 and N > next_col >= 0\
                and MAP[next_row][next_col]:
            union(row, col, next_row, next_col)

result = 0

while len(origin_set) != 1:
    result += 1
    while civ_que:
        row, col = civ_que.popleft()

        for direction in range(4):
            next_row = row + DY[direction]
            next_col = col + DX[direction]

            if N > next_row >= 0 and N > next_col >= 0:

                if not MAP[next_row][next_col]:
                    MAP[next_row][next_col] = MAP[row][col]
                    next_que.append((next_row, next_col))
                    for next_direction in range(4):
                        nnext_row = next_row + DY[next_direction]
                        nnext_col = next_col + DX[next_direction]

                        if N > nnext_row >= 0 and N > nnext_col >= 0\
                            and MAP[nnext_row][nnext_col]\
                                and MAP[nnext_row][nnext_col] != MAP[next_row][next_col]:
                            union(next_row, next_col, nnext_row, nnext_col)

                elif MAP[next_row][next_col] != MAP[row][col]:
                    union(row, col, next_row, next_col)
    next_que, civ_que = civ_que, next_que

print(result)