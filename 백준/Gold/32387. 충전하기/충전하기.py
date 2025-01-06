import sys
input = sys.stdin.readline
# 각각의 행동이 주어질 때마다 행동의 결과를 한 줄에 하나씩 출력

# 동우는 N개의 포트가 있는 멀티 포트 충전기를 장만함, 각 포트별로 출력해주는 전력이 다르다
# i 번째 포트는 i 만큼의 전력을 출력해 준다
# 동우는 총 Q번 충전기에 꽂거나 뽑을 것이다 구체적으로 하는 행동은 아래 2가지이다.

# 1. i : 최소 전력이 i 인 전자기기를 i 번 포트에 꽂는다 만약 i 번 포트에 전자기기가 있다면
# 최소 전력 이상의 포트 중 가장 전력이 낮은 포트에 꽂음, 만약 남아잇는 모든 포트가 최소 전력 미만이면 꽂지 않음

# 2. i 번 포트에 기기가 꽂혀 있다면 기기를 뽑는다

# 1번 행동 : 기기를 꽂았다면 포트 번호 출력, 꽂지 않았다면 -1 출력
# 2번 행동 : 기기가 꽂혀 있다면 몇 번째 행동에서 꽂힌 기기인지 출력, 꽂혀 있지 않았다면 -1이 출력 (몇 번째 행동인지는 1번 행동 + 2번 행동)

def init(s, e, idx): # 초기화
    if s == e:
        port[idx] = 1
        return port[idx]
    else:
        m = (s + e) // 2
        port[idx] = init(s, m, idx*2) + init(m+1, e, idx*2+1)
        return port[idx]

def update(s, e, idx, num, val): # 포트 연결 변경
    if num < s or num > e:
        return

    if s == e:
        port[idx] += val
        return

    port[idx] += val
    m = (s + e) // 2
    if num <= m:
        update(s, m, idx*2, num, val)
    else:
        update(m+1, e, idx*2+1, num, val)
def find(s, e, idx, num): # 비어있는 포트 찾기
    if port[idx] <= 0 or e < num:
        return float('inf')
    if s == e:
        return s

    m = (s + e) // 2
    left = find(s, m, idx*2, num)
    right = float('inf')
    if left == float('inf'):
        right = find(m+1, e, idx*2+1, num)
    return min(left, right)

# 첫 번째 줄에 포트의 수 N(1 <= N <= 10^6), 행동의 수 Q(1 <= Q <= 10^6)
N, Q = map(int, input().strip().split())

port = [0]*(4*N)
visit = [0]*(N+1)

init(1, N, 1)
# Q줄에 걸쳐 동우가 하는 행동의 타입 t(t = 1 or 2)와 포트 번호 또는 최소 전력을 의미하는 정수 i(1 <= i <= N)
for l in range(1, Q+1):
    t, i = map(int, input().strip().split()) # 행동 타입, 포트 번호 또는 최소 전력

    if t <= 1:
        temp = find(1, N, 1, i)
        if temp == float('inf'):
            print(-1)
        else:
            print(temp)
            update(1, N, 1, temp, -1)
            visit[temp] = l

    else:
        if visit[i]:
            print(visit[i])
            visit[i] = 0
            update(1, N, 1, i, 1)
        else:
            print(-1)

"""
각 포트에 최소 전력이 i 인 전자기기를 i 번 포트에 꽂아야 할 때, i 번 포트가 이미 사용중 이라면
i 보다 크고 비어있는 포트 중 가장 전력이 낮은 포트에 꽂아야 함
"""