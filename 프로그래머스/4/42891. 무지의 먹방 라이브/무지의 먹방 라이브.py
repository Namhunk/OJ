# 1 <= len(food_times) <= 2,000,000
# 1 <= food_times[i] <= 100,000,000
# 1 <= k <= 2 x 10^13
import heapq

def solution(food_times, k):
    # 모든 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # (음식 시간, 음식 번호)를 최소힙에 삽입
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0      # 지금까지 먹은 총 시간
    previous = 0       # 직전에 다 먹은 음식 시간
    length = len(food_times)  # 남은 음식 개수

    # 가장 적게 남은 음식부터 한 번에 제거
    while sum_value + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]   # 현재 최소 음식 시간
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 남은 음식들에 대해 k가 얼마 남았는지
    # k - sum_value 만큼 실제로 한 칸씩 돌아간다고 보면 됨
    # 남은 음식들을 번호 기준으로 정렬
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]

'''
모든 음식들을 1초 동안 번갈아 먹는다 할 때
k초 뒤에 어떤 음식을 먹게 되는가?

만약 모든 음식을 다 먹었다면 -1

결국 K+1 번째 위치는 어디인가를 묻는 문제
만약 food_times의 모든 합이 K보다 작거나 같다면 -1

'''