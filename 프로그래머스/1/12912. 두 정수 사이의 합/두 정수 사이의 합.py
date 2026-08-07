def solution(a, b):
    if a > b:
        a, b = b, a
    answer = sum(range(a, b+1))
    return answer

'''
두 숫자의 부호가 같은경우 b-a
두 숫자의 부호가 다른 경우 b+a

숫자의 합은 a <= num <= b 범위의 값들을 더해야 함

1. 각 a, b의 부호를 확인
2. 
'''