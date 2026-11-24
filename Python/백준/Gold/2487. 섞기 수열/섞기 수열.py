import sys
import random, math
input = sys.stdin.readline

    
def solve(N, arr):
    cnt = set()
    visit = [False]*(N+1)
    for i in range(1, N+1):
        if visit[i]: continue

        L = 0
        j = i
        while not visit[j]:
            visit[j] = True
            j = arr[j]
            L += 1

        cnt.add(L)

    print(math.lcm(*cnt))


def main():
    # 1 <= N <= 20,000
    N = int(input().strip())
    arr = tuple([0]+list(map(int, input().strip().split()))) # 섞기 수열
    solve(N, arr)

if __name__ == '__main__':
    main()

"""
N개의 카드를 정해진 방법으로 섞는다
섞는 방법은 1 ~ N까지 숫자로 이루어진 수열로 표시

현재 가지고 있는 카드에서 섞기 수열의 각 숫자가 나타내는 위치에 있는 카드를 뽑아서 나열

예제 1
N = 6
[3, 2, 5, 6, 1, 4]

[1, 2, 3, 4, 5, 6]
[3, 2, 5, 6, 1, 4]
[5, 2, 1, 4, 3, 6]
[1, 2, 3, 6, 5, 4]
[3, 2, 5, 4, 1, 6]
[5, 2, 1, 6, 3, 4]
[1, 2, 3, 4, 5, 6]

1의 위치 이동 1 -> 5 -> 3 -> 1
2의 위치 이동 2 -> 2
3의 위치 이동 3 -> 1 -> 5 -> 3
4의 위치 이동 4 -> 6 -> 4
5의 위치 이동 5 -> 3 -> 1 -> 5
6의 위치 이동 6 -> 4 -> 6

1, 3, 5 는 3번의 사이클
2는 1번
4, 6은 2번의 사이클

3x2 = 6

각 숫자가 몇번만에 자신의 위치로 오는지 각각 구함
만약 현재 숫자가 같은 다른 사이클에 포함된다면 안돌아도 됨
"""