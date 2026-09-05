# 1 <= distance <= 10^9
# 1 <= n <= len(rocks) <= 5x10^4
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    l, r = 1, distance
    while l <= r:
        m = (l + r)//2
        
        cnt = 0 # 현재 몇개의 돌을 제거했는지
        start = 0 # 거리 기준점
        
        for i in range(len(rocks)):
            if rocks[i] - start < m: # 최솟값 기준보다 거리가 작다면 제거
                cnt += 1
            else: # 기준값을 통과한다면 start값 갱신
                start = rocks[i]
        
        if cnt <= n: # n개의 돌보다 덜 제거했다면 최솟값 기준이 낮으므로 l 증가
            answer = m
            l = m + 1
        else: # 너무 많이 제거했다면 r을 줄임
            r = m - 1

    return answer

'''
출발지점에서 distance 만큼 떨어진 곳에 도착지점이 있음
그 사이에는 바위들이 있음
바위 중 몇 개를 제거하려 함

n개의 바위를 제거한 뒤 각 지점 사이 거리의 최솟값 중
가장 큰 것을 return
----------------------------------------------
n개의 바위를 제거하는데 최솟값이 가장 최대가 되는 값

이분탐색
0부터 distance의 값을 이분탐색을 사용해서 해결




'''