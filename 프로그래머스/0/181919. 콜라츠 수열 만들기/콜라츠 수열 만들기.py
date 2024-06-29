def solution(n):
    answer = [n]
    while n != 1:
        if not n % 2: n //= 2
        else: n = 3*n+1
        answer.append(n)
    return answer