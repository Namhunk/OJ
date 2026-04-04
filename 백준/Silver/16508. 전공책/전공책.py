import sys
input = sys.stdin.readline
from string import ascii_letters
def solve():
    # 만들고자 하는 단어 T (1 <= len(T) <= 10)
    T = list(input().strip())
    M = len(T)

    # 전공책의 개수
    N = int(input().strip())

    # 각 전공책 정보 저장 배열
    BOOKS = []

    # 전공책 가격 C (10,000 <= C <= 100,000), 제목 W (1 <= len(W) <= 50)
    for _ in range(N):
        C, W = input().strip().split()
        BOOKS.append((int(C), W))
    
    DP = [float('inf')]*(1 << M)
    DP[0] = 0

    for C, W in BOOKS:
        for state in range((1 << M)-1, -1, -1):
            if DP[state] == float('inf'): continue

            n_state = state
            book_c = list(W)
            
            for i in range(M):
                if not (n_state & (1 << i)):
                    if T[i] in book_c:
                        book_c.remove(T[i])
                        n_state |= (1 << i)
            
            DP[n_state] = min(DP[n_state], DP[state] + C)
    
    print(DP[-1] if DP[-1] != float('inf') else -1)



if __name__ == '__main__':
    solve()

"""
[(35000, 5), (40000, 7), (43000, 6), (47000, 5)]
여러개의 전공책들이 있을때 전공책들의 제목만을 오려내어
원하는 단어를 만드려고 할 때 전공책 가격의 최솟값
만약 단어를 만들 수 없다면 -1 출력

각 구성의 CASE마다 최솟값을 구함
예를들어

예제 1의 경우

포함하지 않는 경우 = 000
A 만 포함 = 100
N 만 포함 = 010
T 만 포함 = 001

A, N 포함 = 110
A, T 포함 = 101
N, T 포함 = 011

A, N, T 포함 = 111
의 경우들이 있음

이때 각 경우의 최솟값을 구함
-------------------------------------------------
1. 각 책의 제목이 어떤 idx를 가지고 있는지 확인(idx는 원하는 단어의 필요 알파벳으로 구성한 숫자)
2. 각 자리마다 가격의 최솟값
3. 
"""