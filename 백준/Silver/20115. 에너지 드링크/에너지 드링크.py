import sys
input = sys.stdin.readline

def solve():
    # 에너지 드링크 수 N (2 <= N <= 10**5)
    N = int(input().strip())
    drink = sorted(map(int, input().strip().split()))

    # 가장 큰 숫자에 작은 숫자들을 사용
    ans = drink[N-1]
    for i in range(N-1):
        ans = ans + (drink[i]/2)
    
    print(ans)

if __name__ == '__main__':
    solve()
"""
1. 임의의 서로 다른 두 에너지 드링크를 고름
2. 한쪽 에너지 드링크를 다른쪽에 모두 붓는다(페인은 붓는 과정에서 원래 양의 절반을 바닥에 흘림)
3. 다 붓고 나머지 빈 에너지 드링크는 버림
4. 1-3 과정을 1개만 남을때까지 반복

최대로 만들 수 있는 에너지 드링크의 양을 출력

결국 드링크는 1개까지 남겨야 함
"""