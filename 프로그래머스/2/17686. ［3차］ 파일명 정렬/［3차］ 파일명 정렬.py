import re
def solution(files):
    answer = []
    
    info = [] # 각 정보를 저장
    for i, f in enumerate(files):
        head   = re.search(r'(^[^0-9]+)', f).group(1)      # 앞쪽에 위치하고 숫자가 아닌 그룹
        number = re.search(rf'{head}([0-9]+)', f).group(1) # head 다음에 오는 숫자
        head = head.lower() # 대문자 -> 소문자로 통일
        info.append((head, int(number), i))
    
    info.sort()
    for _, _, i in info:
        answer.append(files[i])
    return answer

'''
파일명은 HEAD, NUMBER TAIL 3가지로 구성됨

1. HEAD 기준으로 사전 순 정렬 대소문자 구분을 하지 않음
2. NUMBER 숫자 순 정렬
3. HEAD, NUMBER가 같은 경우 원래 순서를 유지

--------------------------------------------------

'''