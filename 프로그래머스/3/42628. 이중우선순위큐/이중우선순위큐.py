from heapq import heappush, heappop
def solution(operations):
    min_heap = [] # 최소 순서
    max_heap = [] # 최대 순서
    visit = [] # 이미 제외된 숫자인지
    cnt = 0 # 삽입 순서
    
    for row in operations:
        t, n = row.split()
        
        if t == 'I':
            heappush(min_heap, (int(n), cnt))
            heappush(max_heap, (-int(n), cnt))
            visit.append(False)
            cnt += 1
        else:
            
            if n == '-1' and min_heap:
                k = heappop(min_heap)
                visit[k[1]] = True
            elif n == '1' and max_heap:
                k = heappop(max_heap)
                visit[k[1]] = True
            
            while min_heap and visit[min_heap[0][1]]:
                heappop(min_heap)
            
            while max_heap and visit[max_heap[0][1]]:
                heappop(max_heap)
    
    answer = [0, 0]
    if min_heap:
        k = heappop(min_heap)
        answer[0] = k[0]
        answer[1] = k[0]
        
    while min_heap:
        k = heappop(min_heap)
        if visit[k[1]]:
            continue
        
        answer[0] = max(answer[0], k[0])
        answer[1] = min(answer[1], k[0])
        
    return answer

"""
I 숫자 : 큐에 숫자를 삽입
D 1 : 큐에서 최댓값을 삭제
D -1 : 큐에서 최솟값을 삭제

16, -5643
16


"""