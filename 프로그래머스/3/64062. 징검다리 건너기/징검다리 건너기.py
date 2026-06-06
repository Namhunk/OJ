# 1 <= len(stones) <= 200,000
# 1 <= stones[i] <= 200,000,000
# 1 <= k <= len(stones)
def solution(stones, k):
    n = len(stones)
    # 이분탐색으로 해결
    l, r = 0, max(stones) # 현재 지나는 인원 수
    while l < r:
        m = (l + r) // 2
        
        curr = 0
        
        # m명이 징검다리를 지나갈 때 바위의 num이 m보다 작은 경우
        for i in range(n):
            if curr >= k: break
            if stones[i] <= m:
                curr += 1
            else:
                curr = 0
        
        if curr < k:
            l = m + 1
        else:
            r = m
            
    answer = l
    return answer

"""
1. 각 stones의 위치를 지날때 마다 숫자가 1씩 줄어들음
2. 0이되면 더이상 밟을 수 없음, 다음 돌로 건너 뛸 수 있음
3. 밟을 수 있는 돌이 여러 개인 경우 가장 가까운 돌로만 이동 가능

최대 몇 명까지 건널 수 있는지 return

-------------------------------------------------------------

모든 돌을 지나간다고 했을 때 
돌 사이의 간격이 k가 넘는 시점을 구해라

"""