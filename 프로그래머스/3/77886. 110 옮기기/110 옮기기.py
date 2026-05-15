def solution(s):
    answer = []
    for x in s:
        ret = change_number(x)
        answer.append(ret)
        
    return answer

def change_number(x):
    stack = []
    cnt = 0
    for i in x:
        stack.append(i)
        
        while len(stack) > 2 and stack[-3:] == ['1', '1', '0']:
            for _ in range(3):
                stack.pop()
            cnt += 1
    
    remain = ''.join(stack)
    idx = remain.rfind('0')
    if idx == -1:
        result = '110' * cnt + remain
    else:
        result = remain[:idx + 1] + '110' * cnt + remain[idx + 1:]
    return result

    
"""

1, 0 으로만 구성된 N개의 문자가 주어졌을 때
문자열에 110이 존재한다면 해당 부분을 임의의 위치에 삽입할 수 있음
각 문자열마다 사전순으로 가장 앞에오는 0, 1 배치를 찾아서 return

-------------------------------------------------------------
2진수 배열이 주어졌을때 가장 숫자가 작게 나오도록


"""