# 1 <= len(jobs) <= 500
from heapq import heappush, heappop
def solution(jobs): # jobs[i] = [요청시간, 소요시간]
    N = len(jobs)   # 배열 크기
    jobs = sorted(jobs) # 요청 시간 순 정렬
    
    idx = 0
    last = -1
    curr = 0
    heap = []
    answer = 0
    
    while idx < N:
        for i in range(idx, N):
            if last < jobs[i][0] <= curr:
                heappush(heap, (jobs[i][1], jobs[i][0]))
            elif jobs[i][0] > curr:
                break
        
        if heap:
            e, s = heappop(heap)
            last = curr
            curr += e
            answer += (curr - s)
            idx += 1
        else:
            curr += 1
            
    return answer // N

"""
작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높음

----------------------------------------------------------------------------------------
1. 작업은 하나씩 처리


"""