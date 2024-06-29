def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if not included[i]: continue
        answer += (a + d * i)
    return answer