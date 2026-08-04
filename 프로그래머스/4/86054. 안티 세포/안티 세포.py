def solution(a, s):
    answer = []
    
    start = 0
    for end in s:
        b = a[start: start+end]
        start += end
        answer.append(get_cnt(b))
        
    return answer

def get_cnt(arr):
    n = len(arr)
    MOD = 10**9 + 7
    dp = []
    
    for i in range(n):
        cur = {}
        
        if i == 0:
            base_count = 1
        else:
            base_count = sum(c for c, _ in dp[i - 1].values()) % MOD
            
        cur[arr[i]] = (base_count, i)

        # (2) 왼쪽 블록과 합이 같으면 합쳐서 합이 2배, 4배, 8배, ... 로
        #     커지는 상태들을 연쇄적으로 만들어 붙임
        T = arr[i]
        while True:
            cnt_cur, j = cur[T]          # 현재 블록 [j, i]의 합 = T
            prev_idx = j - 1
            if prev_idx < 0:
                break
            prev_map = dp[prev_idx]
            if T not in prev_map:
                break                     # 왼쪽에 합이 같은 블록이 없으면 더 못 합침

            cnt_prev, prev_start = prev_map[T]
            newT = T * 2
            # 합쳐진 새 블록: [prev_start, i], 합 = newT
            cur[newT] = (cnt_prev, prev_start)
            T = newT

        dp.append(cur)

    return sum(c for c, _ in dp[-1].values()) % MOD
'''
서로 다른 배열 c의 개수

배열을 입력 했을 때
나올수 있는 경우를 계산하는 함수가 필요

연속된 두 범위의 숫자 합을 확인

0 0 0 0
0 0 0 0
0 0 0 0

'''