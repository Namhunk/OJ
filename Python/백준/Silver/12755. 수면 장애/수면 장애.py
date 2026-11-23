import sys
input = sys.stdin.readline

    
def solve():
    pass

def main():
    N = int(input().strip())-1

    # 1. 현재 자릿수 위치
    k = 10
    r = 0

    while N >= (k-1)*(k**r)*(r+1):
        N -= (k-1)*(k**r)*(r+1)
        r += 1

    # r+1 자리의 숫자
    # 이때 N // (r+1)이 해당 값의 숫자, N % (r+1) 뒤로가는 크기
    div = N//(r+1)
    mod = N%(r+1)
    num = str(10**r + div)
    print(num[mod])
    


if __name__ == '__main__':
    main()
"""
N번째 숫자를 구해라

1자리 9x1
2자리 9x10x2
3자리 9x10x10x3
4자리 9x10x10x10x4

r+1 자리 숫자
"""