import sys
input = sys.stdin.readline

# 주어진 연산을 K번 했을 때, 만들 수 있는 가장 큰 수를 출력, 연산을 K번 할 수 없으면 -1 출력

# 0으로 시작하지 않는 정수 N이 있고 M을 정수 N의 자릿수라고 했을 떄,
# 1 <= i < j <= M 인 i, j를 고르고 각 i, j 위치의 숫자를 바꾸는 연산을 K번 수행할 떄 나올 수 있는 수의 최대값

# N, K 입력 (1 <= N <= 1,000,000), (1 <= K <= 10)
N, K = map(int, input().strip().split())
M = len(str(N)) # 자릿수 크기

from collections import deque
def solve(N, K):
    visit = set() # 중복 방지
    visit.add((N, 0))
    que = deque([(N, 0)])
    ans = 0

    while que:
        num, k = que.popleft()
        if k == K: # 모든 연산 횟수를 사용했다면
            ans = max(ans, num)
            continue

        num = list(str(num))
        for i in range(M-1): # 0 - (M-1)
            for j in range(i+1, M): # 1 - (M-1)
                if i == 0 and num[j] == '0': continue # i, j 바꿨을때 0번 위치가 0이 아닐때만
                num[i], num[j] = num[j], num[i]
                next_num = int(''.join(num))
                if (next_num, k+1) not in visit:
                    que.append((next_num, k+1))
                    visit.add((next_num, k+1))

                num[i], num[j] = num[j], num[i]

    return ans if ans else -1

print(solve(N, K))

"""
연산중 맨 앞 위치에 0이 오면 안됨
모든 위치에 대해 변경이 끝나고 K가 남으면
홀, 짝에 대해서 2가지로 결과를 구분


"""