INF = 10**9

def solution(beginning, target):
    R = len(beginning)
    C = len(beginning[0])
    
    answer = INF
    
    for mask in range(1 << R): # 뒤집을 행 선택
        row_cnt = bin(mask).count('1')
        
        col_cnt = 0
        ok = True
        
        for c in range(C):
            same = True
            opposite = True
            for r in range(R):
                cur = beginning[r][c]
                if (mask >> r) & 1: # 현재 행이 선택된 경우
                    cur ^= 1
                
                if cur != target[r][c]:
                    same = False
                if (cur^1) != target[r][c]:
                    opposite = False
                
            if not same and not opposite:
                ok = False
                break
            elif opposite:
                col_cnt += 1
        
        if ok:
            answer = min(answer, row_cnt + col_cnt)

    return answer if answer != INF else -1