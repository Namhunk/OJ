import sys
input = sys.stdin.readline

def solve():
    # 스위치의 개수 (1 <= N <= 100)
    N = int(input().strip())

    # 스위치의 상태
    S = [0]+list(map(int, input().strip().split()))

    # 학생 수 (1 <= C <= 100)
    C = int(input().strip())
    
    # 각 학생의 동작
    for _ in range(C):
        G, D = map(int, input().strip().split()) # 성별, 숫자

        if G == 1: # 남자
            S = Man(D, N, S)

        elif G == 2: # 여자
            Woman(D, N, S)
    
    for i in range(1, N+1, 20):
        s = i
        e = min(N+1, i+20)
        print(*S[s: e])

def Man(num, N, S):
    for i in range(num, N+1, num):
        S[i] ^= 1
    
    return S

def Woman(num, N, S):
    l, r = num, num

    while 0 < l-1 and r+1 < N+1:
        if S[l-1] == S[r+1]:
            l -= 1
            r += 1
        else:
            break
    
    for i in range(l, r+1):
        S[i] ^= 1
    
if __name__ == '__main__':
    solve()

"""
1부터 N까지의 번호가 붙은 스위치가 존재함
스위치는 on=1 또는 off=0 상태

남학생은 스위치 번호가 자기가 받은 수의 배수이면 상태를 바꿈 3을 받으면 3, 6, 9, ...
여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 
포함한 구간을 찾아, 그 구간에 속한 스위치의 상태를 바꿈, 이때 구간에 속한 스위치의 개수는 홀수

과정을 수행한 후의 결과를 출력 한줄에 최대 20개의 스위치까지 출력
"""