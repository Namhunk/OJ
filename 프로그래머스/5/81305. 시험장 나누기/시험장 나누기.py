import sys
sys.setrecursionlimit(10**6)

def solution(k, num, links):
    N = len(num)
    find_root = {i for i in range(N)}
    for i in range(N):
        for child in links[i]:
            if child != -1:
                find_root.discard(child)
    
    root = find_root.pop()
    
    # 1. 후위 순회 결과를 담을 배열 (solution 내부 지역 변수로)
    arr = []
    
    # 내부 함수로 만들어서 arr, links에 쉽게 접근하도록 함
    def postorder(x):
        left, right = links[x]
        if left >= 0:
            postorder(left)
        if right >= 0:
            postorder(right)
        arr.append(x)
        
    postorder(root)
    
    # 2. 이분 탐색용 판별 함수
    def group_cnt(limit):
        sum_dp = [0]*N
        cnt_dp = [0]*N
        
        for x in arr: # 무조건 후위 순회 순서대로 안전하게 접근
            left, right = links[x]
            a = num[x]
            
            # 자식이 없는 리프
            if left < 0 and right < 0:
                sum_dp[x] = a
                cnt_dp[x] = 0
                continue
            
            # 자식이 1명
            if (left >= 0) ^ (right >= 0):
                child = left if left >= 0 else right
                s, c = sum_dp[child], cnt_dp[child]
                
                if s + a <= limit:
                    sum_dp[x] = s + a
                    cnt_dp[x] = c
                else:
                    sum_dp[x] = a
                    cnt_dp[x] = c + 1
                continue
            
            # 자식이 2명
            if left >= 0 and right >= 0:
                s1, c1 = sum_dp[left], cnt_dp[left]
                s2, c2 = sum_dp[right], cnt_dp[right]
                
                # 셋 다 합칠 수 있는지
                if s1 + s2 + a <= limit:
                    sum_dp[x] = s1 + s2 + a
                    cnt_dp[x] = c1 + c2
                else:
                    # 셋은 안 되고 둘씩 묶을 수 있는지 확인
                    temp = []
                    if s1 + a <= limit:
                        temp.append((s1 + a, s2, c1, c2))
                    if s2 + a <= limit:
                        temp.append((s2 + a, s1, c2, c1))
                    
                    if temp:
                        temp.sort(key=lambda item: item[0])
                        new_sum, other_sum, c_main, c_other = temp[0]
                        sum_dp[x] = new_sum
                        # ★ 여기서 잘려나간 other_sum에 대한 그룹 수 +1 을 꼭 해줘야 함
                        cnt_dp[x] = c_main + c_other + 1 
                    else:
                        # 어느 쪽과도 합칠 수 없으면 두 자식 그룹 다 끊어내고 나 홀로 새 그룹
                        sum_dp[x] = a
                        cnt_dp[x] = c1 + c2 + 2 
                        
        return cnt_dp[root] + 1
    
    # 3. 이분 탐색
    l, r = max(num), sum(num)
    answer = r
    
    while l <= r:
        m = (l + r) // 2
        if group_cnt(m) <= k:
            answer = m
            r = m - 1
        else:
            l = m + 1
            
    return answer