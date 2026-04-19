import sys
input = sys.stdin.readline

import re
def solve():
    # N 파일의 개수 (1 <= N <= 100)
    N = int(input().strip())
    l, r = input().strip().split('*')

    P = re.compile(re.escape(l) + '.*' + re.escape(r))
    for _ in range(N):
        # len(S) <= 100
        S = input().strip()
        if P.fullmatch(S):
            print('DA')
        else:
            print('NE')

if __name__ == '__main__':
    solve()

"""
N개의 줄에 걸쳐
입력으로 주어진 i 번째 파일이 패턴과 일치하면 "DA" 일치하지 않으면 "NE"를 출력한다

별표는 문자열의 시작과 끝에 없음

"""