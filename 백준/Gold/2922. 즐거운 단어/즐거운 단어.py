import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

def solve(word):
    memo = {} # 진행상태 저장

    # 현재 위치, 모음 개수, 자음 개수, L 포함 여부
    def dfs(idx, v_cnt, c_cnt, has_l):
        # 자음, 모음이 연속된 경우 0 반환
        if v_cnt >= 3 or c_cnt >= 3:
            return 0
        
        # 마지막 단어를 통과한 경우
        if idx == len(word):
            return 1 if has_l else 0
        
        # 현재 상태가 이미 존재하는지
        state = (idx, v_cnt, c_cnt, has_l)
        if state in memo:
            return memo[state]
        
        ans = 0
        char = word[idx]
        
        # 밑줄인 경우 3가지로 나뉨
        if char == '_':
            ans += 5 * dfs(idx + 1, v_cnt + 1, 0, has_l)    # 모음
            ans += 20 * dfs(idx + 1, 0, c_cnt + 1, has_l)   # 자음
            ans += 1 * dfs(idx + 1, 0, c_cnt + 1, True)     # L
            
        # 이미 정해진 문자인 경우
        else:
            if char in vowel: # 모음인 경우
                ans += dfs(idx + 1, v_cnt + 1, 0, has_l)
            elif char == 'L': # L인 경우
                ans += dfs(idx + 1, 0, c_cnt + 1, True)
            else: # L이 아닌 자음인 경우
                ans += dfs(idx + 1, 0, c_cnt + 1, has_l)
                
        # 계산 결과 메모이제이션에 저장 후 반환
        memo[state] = ans
        return ans
    
    return dfs(0, 0, 0, 0)
    
if __name__ == '__main__':
    vowel     = set(['A', 'E', 'I', 'O', 'U']) # 모음
    # len(word) <= 100, 
    word = list(input().strip())
    print(solve(word))
    

"""
밑 줄을 알파벳으로 바꿔 즐거운 단어를 만들 수 있는 경우의 수를 출력

밑 줄의 위치에 알파벳을 추가해 즐거운 단어로 만들어야 함

즐거운 단어란 모음(A, E, I, O, U)이 연속해서 3번, 자음(모음을 제외한 나머지)이 연속해서 3번
나오지 않아야 함. 또, L을 반드시 포함해야 함

"""