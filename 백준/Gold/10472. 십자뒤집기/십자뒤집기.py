import sys
input = sys.stdin.readline

def solve():
    arr = []
    for _ in range(3):
        row = input().strip()
        for c in row:
            if c == '.':
                arr.append(0)
            else:
                arr.append(1)
    
    arr = tuple(arr)
    visit = set()
    visit.add(((0,)*9, 0))

    for i in range(3):
        for j in range(3):
            temp = set()
            for k, cnt in visit:
                ret = f(i, j, list(k))
                temp.add((ret, cnt+1))

            visit = visit | temp

    ans = float('inf')
    for k, cnt in visit:
        if arr == k:
            ans = min(ans, cnt)
    
    print(ans)

def f(x, y, k):
    side = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    for r, c in side:
        nx, ny = x+r, y+c
        if not (0 <= nx < 3 and 0 <= ny < 3): continue
        idx = nx * 3 + ny
        k[idx] ^= 1
    
    return tuple(k)


if __name__ == '__main__':
    # P(0 < P <= 50) 테스트 케이스 수
    P = int(input().strip())
    for _ in range(P):
        solve()

"""
3x3 크기의 보드에서 각 칸에 무작위의 색상이 들어옴

이때 하나의 칸을 클릭하면 인접한 상하좌우 4칸의 색상이 함께 바뀜
흰 보드를 입력에 주어진 보드로 바꾸는 데 필요한 최소 클릭 횟수

*: 검정
.: 흰색

1. 바꾸는 경우
2. 놔두는 경우

"""