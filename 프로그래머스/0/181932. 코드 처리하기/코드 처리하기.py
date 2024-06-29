def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if code[i] == '1': mode ^= 1; continue
        if not mode:
            if not i % 2: ret += code[i]
        else:
            if i % 2: ret += code[i]
    answer = ret if len(ret) else 'EMPTY'
    return answer