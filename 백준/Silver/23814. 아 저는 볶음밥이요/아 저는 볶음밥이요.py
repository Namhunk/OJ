import sys
input = sys.stdin.readline

def solve():
    # D(1 <= D <= 10**18) 군만두 서비스를 제공하는 주문의 수
    D = int(input().strip())

    # N, M, K (1 <= N, M, K <= 10**18) # 짜장, 짬뽕, 남은 사람 수 
    N, M, K = map(int, input().strip().split())

    req_n = (D - N % D) % D
    req_m = (D - M % D) % D

    max_cnt = -1
    max_k   = -1
    # 0: 안넘김, 1: 짜장에만, 2: 짬뽕에만, 3: 모두
    for i in range(4):
        cur_n, cur_m, cur_k = N, M, K

        # 짜장에 넘김
        if i == 1 or i == 3:
            if cur_k >= req_n: # 현재 K가 N의 필요 개수보다 많은 경우
                cur_k -= req_n
                cur_n += req_n
            else:
                continue
        
        # 짬뽕에 넘김
        if i == 2 or i == 3:
            if cur_k >= req_m: # 현재 K가 M의 필요 개수보다 많은 경우
                cur_k -= req_m
                cur_m += req_m
            else:
                continue
        
        # 현재 만두의 개수
        G = (cur_n//D) + (cur_m//D) + (cur_k//D)

        if G > max_cnt: # 최대 만두 개수보다 많다면
            max_cnt = G
            max_k   = cur_k
        
        elif G == max_cnt:
            max_k = max(max_k, cur_k)
    
    print(max_k)

if __name__ == '__main__':
    solve()

"""
N + M + K 명이 받는 군만두의 개수를 최대로 하여 시킬 수 있는 볶음밥의 최대 개수

같은 메뉴 D개 당 군만두를 서비스로 줌

볶음밥 10 = 4개
볶음밥 9  = 5개
볶음밥 7  = 5개

1. 넘기지 않는다
2. 짜장에만 넘긴다
3. 짬뽕에만 넘긴다
4. 짜장, 짬뽕 둘다 넘긴다



"""