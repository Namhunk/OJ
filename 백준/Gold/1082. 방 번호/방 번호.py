import sys
input = sys.stdin.readline

# 입력 처리
N = int(input().strip())  # 사용할 수 있는 숫자 개수
P = list(map(int, input().strip().split()))  # 각 숫자의 가격
M = int(input().strip())  # 사용할 수 있는 최대 금액

# (가격, 숫자) 튜플로 정렬 (가격 낮고 숫자 큰 순서)
arr = sorted([(P[i], i) for i in range(N)], key=lambda x: (x[0], -x[1]))

ans = []
curr = 0

if N == 1:
    # 사용할 수 있는 숫자가 1개뿐인 경우
    cost, digit = arr[0]
    if cost > M:
        print(0)
        exit()
    count = M // cost
    ans = [digit] * count
else:
    # 사용할 수 있는 숫자가 여러 개인 경우

    # 맨 앞자리 처리
    if arr[1][0] > M:
        # 2번째로 싼 숫자도 못 사면 가장 싼 거라도 써야 함
        if arr[0][0] > M:
            print(0)
            exit()
        ans.append(arr[0][1])
        curr += arr[0][0]
    else:
        if arr[0][1] == 0:
            # 가장 싼 숫자가 0이면 앞자리에 쓸 수 없으므로 2번째로 싼 숫자 사용
            ans.append(arr[1][1])
            curr += arr[1][0]
        else:
            ans.append(arr[0][1])
            curr += arr[0][0]

    # 뒤에 자릿수 최대한 붙이기
    while curr + arr[0][0] <= M:
        ans.append(arr[0][1])
        curr += arr[0][0]

    # 더 큰 숫자로 바꿔치기 (가격 범위 내에서)
    for i in range(len(ans)):
        for cost, num in arr:
            if i == 0 and num == 0:
                continue  # 앞자리에 0 안됨
            if num > ans[i] and curr - P[ans[i]] + cost <= M:
                curr = curr - P[ans[i]] + cost
                ans[i] = num

# 출력
res = ''.join(map(str, ans))
print(int(res))