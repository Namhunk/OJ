import sys
input = sys.stdin.readline

# 가장 많은 고층 빌딩이 보이는 빌딩을 구하고, 거기서 보이는 빌딩의 수를 출력
def func(idx):
    result = 0 # 현재 위치의 최대값 저장
    height = H[idx] # 현재 높이
    for i in range(N):
        x = i-idx # x 거리
        y = height-H[i] # y 거리
        if x == 0: continue # 현재 지점과 같지 않을 때
        grad = y/abs(x) # 현재 위치와 i 의 기울기
        k = (-1 if x > 0 else 1) # i가 현재 값보다 작으면 + 크면 -
        flag = 1 # 거리 체크
        for j in range(i+k, idx, k): # i ~ idx 사이 건물
            if H[j] >= H[i]+grad*abs(j-i): # j 위치의 건물의 높이가 j 위치의 선분을 지나는 점보다 크거나 같으면 x
                flag = 0
                break
        if flag:
            result += 1

    return result

N = int(input().strip()) # 빌딩의 개수 1 <= N <= 50
H = list(map(int, input().strip().split())) # 높이는 1e9 보다 작거나 같은 자연수

ans = 0
for i in range(N):
    ans = max(ans, func(i))

print(ans)