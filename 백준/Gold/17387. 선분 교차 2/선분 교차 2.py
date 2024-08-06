import sys
input = sys.stdin.readline

# 2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때 두 선분이 교차하는지 아닌지 구해라
# L1과 L2가 교차하면 1, 아니면 0을 출력한다

# -1,000,000 <= x1, y1, x2, y2, x3, y3, x4, y4 <= 1,000,000

# L1의 양 끝점 x1, y1, x2, y2
L1 = list(map(int, input().strip().split()))

# L2의 양 끝점 x3, y3, x4, y4
L2 = list(map(int, input().strip().split()))

# CCW 알고리즘을 사용하여 세 점의 대한 벡터의 외적을 구해봄
def CCW(ax, ay, bx, by, cx, cy):
    return (bx-ax)*(cy-by) - (cx-bx)*(by-ay)

def solv(L1, L2):
    x1, y1, x2, y2 = L1
    x3, y3, x4, y4 = L2

    res1 = CCW(x1, y1, x2, y2, x3, y3)
    res2 = CCW(x1, y1, x2, y2, x4, y4)
    res3 = CCW(x1, y1, x3, y3, x4, y4)
    res4 = CCW(x2, y2, x3, y3, x4, y4)

    if res1*res2 == 0 and res3*res4 == 0: # 평행할때
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return 1
    else: # 교차할때
        if res1*res2 <= 0 and res3*res4 <= 0:
            return 1
    return 0

print(solv(L1, L2))