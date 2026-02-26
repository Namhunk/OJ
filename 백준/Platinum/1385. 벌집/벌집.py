import sys
input = sys.stdin.readline

from math import ceil, floor
from heapq import heappush, heappop
def solve(a, b):
    # 현재 위치 a, 출구 b (1 <= a, b <= 1,000,000)
    if a == b: # a, b가 같은 경우
        return [a]
    
    MAX_SIZE = 1_000_000
    visit = [float('inf')]*(MAX_SIZE+1)
    visit[a] = 0

    dist = {0: set([a])}
    heap = [[0, a]]
    while heap:
        cnt, x = heappop(heap)
        if x == b:
            break

        for nx in neighbors(x):
            if nx <= MAX_SIZE and visit[nx] == float('inf'):
                visit[nx] = cnt+1
                heappush(heap, (visit[nx], nx))

                if visit[nx] in dist.keys():
                    dist[visit[nx]].add(nx)
                else:
                    dist[visit[nx]] = set([nx])

    ans = [b]
    curr = b
    for i in range(visit[b]-1, -1, -1): # 역순으로 탐색
        num = min(dist[i].intersection(neighbors(curr)))
        ans.append(num)
        curr = num
    return ans[::-1]

def neighbors(x): # 현재값의 이웃 6개를 찾는 함수
    if x == 1: # 1인 경우
        return set(range(2, 8)) # 2부터 7까지 반환
    else:
        s, i, k = start_idx_floor(x)

        # 최종 반환할 6개의 숫자를 가진 list
        ret = [0]*6

        # 같은 층의 이웃한 숫자 2개
        ret[0]  = s+(i-1)%(6*k)
        ret[1] = s+(i+1)%(6*k)

        # 현재 위치가 k로 나누어 떨어지면 위층 3개, 아래층 1개
        # 반대면 위층 2개 아래층 2개

        # 아랫층 2개 먼저 구함
        if k == 1: # k가 1인 경우 이전층은 모두 1만 존재
            ds_left  = 1
            ds_right = 1
        else:
            ds_left  = s-(6*(k-1))+ceil(i/k*(k-1)-1)%(6*(k-1))
            ds_right = s-(6*(k-1))+ceil(i/k*(k-1))%(6*(k-1))

        # 윗층 3개
        us_left  = int(s+(6*k)+(i/(k)*(k+1))%(6*(k+1)))
        us_mid   = int(s+(6*k)+(i/(k)*(k+1)+1)%(6*(k+1)))
        us_right = int(s+(6*k)+(i/(k)*(k+1)+2)%(6*(k+1)))

        if (i+1) % k == 0: # k로 나누어 떨어지면 아랫층 1개 윗층 3개
            ret[2] = ds_left
            ret[3] = us_left
            ret[4] = us_mid
            ret[5] = us_right
        
        else: # 반대는 아랫층 2개 윗층 2개
            ret[2] = ds_left
            ret[3] = ds_right
            ret[4] = us_left
            ret[5] = us_mid
        
        return set(ret)

def start_idx_floor(x): # 현재 x의 시작 숫자 s, x의 위치 i, x의 층 k
    k = 1
    s, e = 3*k*(k-1)+2, 3*k*(k+1)+2
    while x not in range(s, e):
        k += 1
        s = 3*k*(k-1)+2
        e = 3*k*(k+1)+2
    
    return s, x-s, k         

if __name__ == '__main__':
    import random
    a, b = map(int, input().strip().split())
    print(*solve(a, b))

"""
모든 경로를 생성하는건 메모리 초과
그럼 해당 경로에서 다음으로 갈 수 있는 경로를 그때그떄 계산해서 추가하는 방법으로


출구를 최단거리로 지나갈때 지나온 방의 번호를 출력

각 중앙이 0층 중앙을 둘러싼 방들이 1층이라 할 때
총 k개의 층이 존재하고
각 층마다 방의 개수는 6*k임

각 층의 방의 범위는
f(1) = 2
f(2) = 8
f(3) = 20
f(n) = 3n(n-1)+2
range( 3n(n-1)+2, 3n(n+1)+2 )

k = floor
s = 3n(n-1)+2
e = 3n(n+1)+2

같은 층에서 이웃한 두 방을 고르는 기준
일단 형태는 (i-1), (i+1)를 챙겨야 함
또한 현재 범위에 대해 이웃을 찾는 것 이므로 s 도 사용
총 숫자는 6k 만큼 등장

left  = s + (i-1) % 6k
right = s + (i+1) % 6k

현재 층에서 이전층의 방을 고르는 기준
숫자가 0부터 증가할 때
k = 1일때 모두 1
k = 2일때 9, 11, 13, ...19는 1개 나머지는 2개
(i + 1) % k == 0 일때 이전 층 1개만 이웃, 나머지는 2개

이때의 방 번호
이전층은 6(k-1)개의 방을 갖고 있음

k 번쨰 숫자는 같은 수가 나와야 하고
k 번째에 (0, 1), (1, 2), (2, 2) 이런식으로 나와야 함

현재 층에서 이전 층의 숫자는 모두 3번씩 등장함
if (i + 1) % k == 0: 은 left만 사용
left  = s-(6*(k-1))+ceil(i/k*(k-1)-1)%(6*(k-1))
right = s-(6*(k-1))+ceil(i/k*(k-1))%(6*(k-1))

다음 숫자를 알아내는 방법
if (i + 1) % k == 0: 은 숫자가 3개
left = s
left  = int(s+(6*k)+(i/(k)*(k+1))%(6*(k+1)))
mid   = int(s+(6*k)+(i/(k)*(k+1)+1)%(6*(k+1)))
right = int(s+(6*k)+(i/(k)*(k+1)+2)%(6*(k+1)))
"""