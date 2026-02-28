import sys
input = sys.stdin.readline

from collections import deque
def solve(word):
    que = deque([(0, 0, 0, 0, 1)])

    ans = 0
    while que:
        idx, v_cnt, c_cnt, has_l, ret = que.popleft()

        if v_cnt >= 3 or c_cnt >= 3: continue

        if idx == len(word):
            if has_l:
                ans += ret
            continue

        if word[idx] == '_':
            que.append((idx+1, v_cnt+1, 0, has_l, ret*5))
            que.append((idx+1, 0, c_cnt+1, 1, ret))
            que.append((idx+1, 0, c_cnt+1, has_l, ret*20))
        
        else:
            if word[idx] in vowel:
                que.append((idx+1, v_cnt+1, 0, has_l, ret))
            elif word[idx] == 'L':
                que.append((idx+1, 0, c_cnt+1, 1, ret))
            else:
                que.append((idx+1, 0, c_cnt+1, has_l, ret))
    
    return ans

    
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