import sys
input = sys.stdin.readline

from collections import deque
def solve():
    vowel = set(['a', 'e', 'i', 'o', 'u']) # 모음
    while 1:
        # 비밀 번호 입력
        password = input().strip()
        if password == "end": break # 만약 입력한 비밀번호가 end면 반복문 종료

        v_cnt, c_cnt     = 0, 0    # vowel, consonant 개수
        before           = ''      # 이전 문자
        con1, con2, con3 = 0, 1, 1 # con1: 모음 포함 여부, con2: 자음, 모음 연속, con3: 연속 중복

        for i in range(len(password)):
            if v_cnt + c_cnt >= 3: # 3개의 문자를 지난 경우
                if password[i-3] in vowel:
                    v_cnt -= 1
                else:
                    c_cnt -= 1
            
            if password[i] in vowel:  # 조건1의 갱신 및 연속된 개수를 더함
                if not con1: con1 = 1
                v_cnt += 1
            else:
                c_cnt += 1
            
            if v_cnt >= 3 or c_cnt >= 3: con2 = 0 # 자음 모음 연속 검사

            if before == password[i]: # 이전과 같은 경우
                if password[i] not in ('e', 'o'): # ee, oo가 아닌 경우
                    con3 = 0
            
            before = password[i]
        
        if con1 and con2 and con3: # 3개의 조건을 모두 만족한 경우
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")

if __name__ == '__main__':
    solve()

"""
비밀 번호를 만드는 조건
1. 모음(a, e, i, o, u) 중 하나 이상을 반드시 포함해야 함
2. 모음이 3개, 자음이 3개 연속으로 오면 안됨
3. 같은 글자가 연속적으로 오면 안됨, 단 ee, oo는 허용

비밀번호의 길이는 1보다 크기만 하면 됨

"""