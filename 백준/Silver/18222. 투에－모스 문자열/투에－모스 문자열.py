import sys
input = sys.stdin.readline

def solve():
    # k(1 <= k <= 10^18)
    k = int(input().strip())

    x = k-1

    ones = x.bit_count()
    print(ones & 1)

if __name__ == '__main__':
    solve()

"""
0, 1 로 이루어진 길이가 무한한 문자열 X가 있음
이 문자열은 다음과 같은 과정으로 만들어짐

1. X는 맨 처음에 "0"으로 시작
2. X에서 0을 1로, 1을 0으로 뒤바꾼 문자열 X'를 만듬
3. X뒤에 X'를 붙인 문자열을 X로 다시 정의
4. 2~3 과정을 무한히 반복

k번째 오는 문자를 출력

"""