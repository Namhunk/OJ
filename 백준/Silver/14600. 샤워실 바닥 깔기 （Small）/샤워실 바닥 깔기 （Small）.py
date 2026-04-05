import sys
input = sys.stdin.readline

tile_num = 1


def fill(board, sx, sy, size, hx, hy):
    global tile_num

    if size == 2:
        num = tile_num
        tile_num += 1

        for i in range(sx, sx + 2):
            for j in range(sy, sy + 2):
                if i == hx and j == hy:
                    continue
                board[i][j] = num
        return

    half = size // 2
    num = tile_num
    tile_num += 1

    mx = sx + half - 1
    my = sy + half - 1

    # 사분면 판별
    # 0: 좌하, 1: 우하, 2: 좌상, 3: 우상
    if hx < sx + half:
        if hy < sy + half:
            quadrant = 2  # 좌상
        else:
            quadrant = 3  # 우상
    else:
        if hy < sy + half:
            quadrant = 0  # 좌하
        else:
            quadrant = 1  # 우하

    centers = [
        (sx + half,     sy + half - 1),  # 좌하의 중앙 쪽 칸
        (sx + half,     sy + half),      # 우하의 중앙 쪽 칸
        (sx + half - 1, sy + half - 1),  # 좌상의 중앙 쪽 칸
        (sx + half - 1, sy + half)       # 우상의 중앙 쪽 칸
    ]

    for q in range(4):
        if q == quadrant:
            continue
        x, y = centers[q]
        board[x][y] = num

    # 각 사분면 재귀
    # 좌하
    if quadrant == 0:
        fill(board, sx + half, sy, half, hx, hy)
    else:
        cx, cy = centers[0]
        fill(board, sx + half, sy, half, cx, cy)

    # 우하
    if quadrant == 1:
        fill(board, sx + half, sy + half, half, hx, hy)
    else:
        cx, cy = centers[1]
        fill(board, sx + half, sy + half, half, cx, cy)

    # 좌상
    if quadrant == 2:
        fill(board, sx, sy, half, hx, hy)
    else:
        cx, cy = centers[2]
        fill(board, sx, sy, half, cx, cy)

    # 우상
    if quadrant == 3:
        fill(board, sx, sy + half, half, hx, hy)
    else:
        cx, cy = centers[3]
        fill(board, sx, sy + half, half, cx, cy)


def solve():
    K = int(input().strip())
    N = 2 ** K

    x, y = map(int, input().strip().split())

    board = [[0] * N for _ in range(N)]
    hx = N - y
    hy = x - 1

    board[hx][hy] = -1

    fill(board, 0, 0, N, hx, hy)

    for row in board:
        print(*row)


if __name__ == "__main__":
    solve()