import sys
input = sys.stdin.readline

# 스택, 자료구조
# 서로 볼 수 있는 쌍의 수를 출력한다

# 두 사람 A, B가 서로 볼 수 있으려면, 두 사람 사이에 A 또는 B 보다 키가 큰 사람이 없어야 함

# 기다리고 있는 사람의 수 N (1 <= N <= 500,000)
N = int(input().strip())

# N개의 줄에 각 사람의 키가 나노미터 단위로 주어짐 모든 사람의 키는 2^31 나노미터 보다 작다
# 사람들이 서 있는 순서대로 입력이 주어짐
arr = [int(input().strip()) for _ in range(N)]

stack = []
ans = 0
for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        ans += stack.pop()[1]

    if not stack:
        stack.append((arr[i], 1))
        continue

    if stack[-1][0] == arr[i]:
        cnt = stack.pop()[1]
        ans += cnt

        if stack:
            ans += 1
        stack.append((arr[i], cnt+1))

    else:
        stack.append((arr[i], 1))
        ans += 1

print(ans)

"""
2 4 1 2 2 5 1
1. 현재 값이 이전 값 보다 크다면 다음 값이 와도 이전 값을 볼 수 없음 = 1 [2,3,..K] ?
2. 현재 값이 이전 값과 같고 다음 값이 현재 값 보다 크다면 다음 값은 (현재, 다음), (이전, 다음) 으로 볼 수 있음 1 1 [2,3,4...K]
3. 현재 값이 이전 값 보다 작다면 현재 값은 이전 값만 볼 수 있고 다음 값은 다시 3가지 경우에 따라 달라짐
"""