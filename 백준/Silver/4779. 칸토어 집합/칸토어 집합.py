import sys
input = sys.stdin.readline

def solve(N):
    global S
    S = list('-'*3**N)
    Replace(0, len(S))
    print(''.join(S))

def Replace(start, curr_size): # 
    if curr_size == 1:
        return 
    next_size = curr_size // 3

    l = start + next_size
    r = start + next_size*2

    for i in range(l, r):
        S[i] = ' '
    
    Replace(start, next_size)
    Replace(r, next_size)

if __name__ == '__main__':
    while 1:
        # N (0 <= N <= 12)
        N = input().strip()
        if N == '': break

        solve(int(N))

"""
0 8

입력 위치는 2개, 왼쪽 끝, 오른쪽 끝
도중에 전체 길이에서 1/3, 2/3 지점을 찾아야 함

0, 9

3,  6

(0, 3), (3, 3), (6, 3)

(0, 1), (1, 1), (2, 1)
(3, 1), (4, 1), (5, 1)


"""