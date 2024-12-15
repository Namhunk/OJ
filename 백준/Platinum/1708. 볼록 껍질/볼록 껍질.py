import sys
input = sys.stdin.readline

# 첫째 줄에 볼록 껍질을 이루는 점의 개수를 출력
# 볼록 껍질의 변에 점이 여러 개 있는 경우에는 가장 양 끝 점만 개수에 포함한다.

# 첫째 줄에 점의 개수 N (3 <= N <= 100,000)
N = int(input().strip())

# 둘째 줄부터 N개의 줄에 걸쳐 각 점의 x, y 좌표가 주어진다 (|x, y| <= 40,000)
# 입력으로 주어지는 다각형의 모든 점이 일직선을 이루는 경우는 없다
point = [list(map(int, input().strip().split())) for _ in range(N)]

# CCW의 값이 음수 : 시계방향, 양수 : 반시계방향, 0 : 한 직선에 놓임
def CCW(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)

def convex_hull(point): # 각 점의 오른쪽에 있는 점 탐색
    point = sorted(point)
    lower = []
    for p in point:
        while len(lower) >= 2 and CCW(*lower[-2], *lower[-1], *p) <= 0: # CCW의 결과 값이 시계방향이거나, 한 직선에 놓인 점인 경우
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(point):
        while len(upper) >= 2 and CCW(*upper[-2], *upper[-1], *p) <= 0:
            upper.pop()
        upper.append(p)

    return len(lower[:-1] + upper[:-1])

print(convex_hull(point))