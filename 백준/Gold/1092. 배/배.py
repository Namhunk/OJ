import sys, math

# 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력, 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력

# N입력 (1 <= N <= 50)
N = int(input().strip())

# 각 크레인의 무게 제한 (0 <= W[i] <= 1,000,000)
WL = sorted(list(map(int, input().strip().split())), reverse=True)

# 박스의 수 M (1 <= M <= 10,000)
M = int(input().strip())

# 각 박스의 무게 (1 <= M <= 1,000,000)
W = sorted(list(map(int, input().strip().split())), reverse=True)

if W[0] > WL[0]: # 박스 무게의 최대값이 크레인 무게제한의 최대값보다 큰 경우
    print(-1)
else:
    ans = 0
    while len(W) > 0:
        ans += 1
        for i in WL:
            for j in range(len(W)):
                if i >= W[j]:
                    del W[j]
                    break

    print(ans)

"""
모든 화물은 박스안에 넣어져 있다
항구에는 크레인 N대가 있고, 1분에 박스를 하나씩 배에 실을 수 있다.
모든 크레인은 동시에 움직인다
"""