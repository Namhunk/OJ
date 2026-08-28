# len(wallet) == len(bill) = 2
# 10 <= wallet[0], wallet[1] <= 100
# 10 <= wallet[0], wallet[1] <= 2,000
def solution(wallet, bill):
    answer = 0
    
    X, Y = wallet # wallet 크기를 가져옴
    A, B = bill   # bill의  크기를 가져옴
    
    # 지갑, 지폐 둘다 큰 숫자가 앞쪽 변수에 오게
    X, Y = sort_desc(X, Y)
    A, B = sort_desc(A, B)

    while X < A or Y < B: # 하나라도 크기가 큰 경우 수행
        answer += 1
        A //= 2 # 큰 쪽의 숫자를 나눔
        A, B = sort_desc(A, B) # 크기에 따라 순서 정렬
    
    return answer

def sort_desc(x, y):
    if x < y:
        x, y = y, x
    
    return x, y
'''
지폐마다 크기가 다름
지폐를 접어서 지갑안에 넣을 수 있음

1. 지폐를 접을 떄는 항상 길이가 긴 쪽을 반으로
2. 접기 전 길이가 홀수였다면 접은 후 소수점은 버림
3. 그대로 또는 90도 회전 해 넣을 수 있다면 그만 접기

----------------------------------------------

'''