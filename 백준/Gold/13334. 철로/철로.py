import sys
input = sys.stdin.readline

# 길이 d의 임의의 선분에 대하여, 집과 사무실 위치가 모두 그 선분에 포함되는 사람들의 최대 수를 한 줄에 출력

# 사람 수를 나타내는 양의 정수 n (1 <= n <= 100,000)
n = int(input().strip())
# 정수 쌍 (hi, oi) (-100,000,000 <= hi, oi <= 100,000,000) 서로 다른 정수
arr = sorted([sorted(list(map(int, input().strip().split()))) for _ in range(n)], key=lambda x: x[1])
# 철로의 길이를 나타내는 정수 d (1 <= d <= 200,000,000)
d = int(input().strip())

from heapq import heappush, heappop
ans = 0 # 최종 값
heap = []
for s, e in arr:
    if (e-s) > d: continue # 집-사무실의 길이가 d 보다 작을 때
    while heap and heap[0][0] < e-d: # 가장 앞에 있는 출발지 위치가 현재 도착지 위치 - d 보다 작을 때
        heappop(heap) # 가장 작은 출발지 제거

    heappush(heap, (s, e))
    ans = max(ans, len(heap)) # 최대 개수 저장

print(ans)