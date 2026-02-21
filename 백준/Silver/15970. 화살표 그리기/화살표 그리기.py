import sys
input = sys.stdin.readline

def solve():
    # 좌표의 개수 N (2 <= N <= 5,000)
    N = int(input().strip())

    # 좌표 x, 색깔 y가 주어짐 (0 <= x <= 1e5, 1 <= y <= N)
    arr = sorted([tuple(map(int, input().strip().split())) for _ in range(N)])
    
    color = {}
    for i in range(N):
        # 위치, 색상
        x, y = arr[i]

        if y not in color.keys():
            color[y] = [x]
        else:
            color[y].append(x)
    MAX = int(1e6)
    ans = 0
    for point in color.values():
        for i in range(len(point)):
            a, b = MAX, MAX # 최댓값으로 설정
            if i-1 > -1: # 이전 위치가 0보다 크면
                a = min(a, abs(point[i] - point[i-1]))
            
            if i+1 < len(point): # 다음 위치가 N의 길이보다 작으면
                b = min(b, abs(point[i] - point[i+1]))
            
            ans += min(a, b)
    
    return ans

if __name__ == '__main__':
    print(solve())
    

"""
- 음수가 아닌 정수의 좌표를 갖는 점들이 N개 주어짐
- 각 점은 N개의 색깔 중 하나를 가지고 있음
- 임의의 점 p에서 연결할 수 있는 점 q는 같은 색상 가장 가까운 같은 색상이어야 함(2개 이상인 경우 아무거나)

모든 점에서 시작하는 화살표들의 길이 합을 출력

결국 모든 N개의 점들에 대해서 i 번째 점일때 같은 색상 중 가장 가까운 점과의 길이들을 구해
모두 더하면 됨

모든 좌표를 거리순으로 정렬하고 
색상별로 구분을 지음 color[k][i] = k 색상에서 i번째
그러면 결국 i번째 좌표에서 가장 가까운 점은 color[k][i-1], color[k][i+1]임

"""