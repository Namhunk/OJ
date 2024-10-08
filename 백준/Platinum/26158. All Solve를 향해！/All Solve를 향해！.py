import sys
input = sys.stdin.readline

# 철민이가 백준 온라인 저지의 모든 문제를 풀기 위해 필요한 날의 수를 출력

# 백준 온라인 저지는 한 페이지에 최대 K개의 문제만을 보여줌(문제의 번호를 기준으로 오름차순 정렬)

# 아래의 방식에 따라 문제를 품
# - 우선, 페이지의 맨 위에 있는 문제를 푼다
# - 그 뒤로, 아래 괴정을 계속 반복한다
# 1. 철민이가 보고있는 페이지를 업데이트
# 2. 그 뒤로, 철민이가 가장 최근에 푼 문제의 난이도가 d일때
# 페이지에 보이는 문제 중 난이도가 d 보다 큰 문제가 있다면 그 문제를 품
# 3. 조건을 만족하는 문제가 여러개라면 맨 위의 문제를 품
# 4. 조건을 만족하는 문제가 없다면 그날의 문제 풀이를 종료

# 문제수 N, 한 페이지에 보이는 문제 수 K (1 <= K <=  N <= 500,000)
N, K = map(int, input().strip().split())

# N개의 문제들의 각각의 난이도 D[i] (1 <= D[i] <= 1e9)
D = list(map(int, input().strip().split()))

# 1. 현재 문제의 난이도가 이전 문제의 난이도 보다 낮다면 무조건 다음 날에 풀어야 함
# 2. 그러면 배열의 난이도는 감소하는 형태를 보임
# 3. 배열의 길이가 늘어난다는 것은 페이지에 보여지는 문제가 늘어나는 것과 비슷 (배열 길이 - 시작 위치 <= K를 만족 해야함)
# 4. 난이도가 감소하는 형태를 보이다 i 번째 문제가 이전 문제보다 크다면 i 번째 문제는 K개의 문제 범위에서 현재 난이도 보다
# 작은 난이도의 문제들 중 가장 큰 문제를 푼 날에 같이 풀게 될 것이다.

temp = [D[0]] # 각 날마다 푼 문제들의 최고 난이도
cnt = [1] # 각 날마다 해결 문제의 수
s = 0 # K 의 범위를 맞추기 위한 시작 위치 설정
SUM = 1 # 쌓인 문제의 총 수
for i in range(1, N):
    if temp[-1] < D[i]: # 현재 난이도가 이전 난이도 보다 크다면
        # 이전의 난이도들 중 현재 난이도 보다 작은 가장 큰 난이도 선택
        l, r = s, len(temp)-1
        while l < r:
            m = (l+r)//2
            if temp[m] >= D[i]: l = m+1
            else: r = m

        temp[l] = D[i] # 해당 위치에 최고 난이도 변경
        cnt[l] += 1 # 해당 날에 푼 문제수 +1
        SUM += 1
    else:
        temp.append(D[i]) # # 페이지에 문제 추가
        cnt.append(1) # 새로운 날에 문제수 +1
        SUM += 1
        # SUM >= K : 다음 날에 풀 문제들의 수의 합이 페이지 수를 넘지 않게

    if SUM - cnt[s] >= K:
        SUM -= cnt[s]
        s += 1

print(len(temp))