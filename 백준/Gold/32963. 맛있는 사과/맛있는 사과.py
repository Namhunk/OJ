import sys
input = sys.stdin.readline

# Q개의 줄에 걸쳐 각 p마다 맛 t[i] 가 p 이상인 사과 중 크기 s[i]가 가장 큰 사과의 개수를 한 줄에 하나씩 순서대로 출력

# 첫 번째 줄에 사과의 개수 N, 질문의 개수 Q가 공백으로 구분되어 주어짐 (1 <= N, Q <= 200,000)
N, Q = map(int, input().strip().split())

# 두 번째 줄에 각 사과의 맛을 나타내는 정수 t[1], t[2], .. t[N]이 공백으로 구분되어 주어짐(1 <= t[i] <= 1,000,000,000)
t = list(map(int, input().strip().split()))

# 세 번째 줄에 각 사과의 크기를 나타내는 정수 s[1], s[2], .. s[N]이 공백으로 구분되어 주어짐(1 <= s[i] <= 1,000,000,000)
s = list(map(int, input().strip().split()))

arr = list(zip(t, s))
arr.sort(key=lambda x: x[0])

t = [i[0] for i in arr]
s = [i[1] for i in arr]

size = [0]*N # 각 맛의 위치에서의 최대 크기
count = [0]*N # 각 최대 크기의 개수

size[-1] = s[-1] # p의 값이 t[i]의 값들 중 가장 큰 값과 같은 경우 가장 큰 크기는 s[-1]
count[-1] = 1

def bisect_left(p):
    l, r = 0, N
    while l < r:
        m = (l+r)//2

        if t[m] < p:
            l = m+1
        else:
            r = m

    return l

for  i in range(N-2, -1, -1): # size[N-1], count[N-1]은 이미 위에서 구함
    if s[i] > size[i+1]: # 현재 s[i] 값이 다음 s[i+1]값 보다 큰 경우
        size[i] = s[i]
        count[i] = 1
    elif s[i] == size[i+1]: # 두 크기가 같은 경우
        size[i] = size[i+1]
        count[i] = count[i+1]+1
    else:
        size[i] = size[i+1]
        count[i] = count[i+1]

# 다음 Q개의 줄에 걸쳐 질문으로 정수 p가 한 줄에 하나씩 주어짐(1 <= p <= 1,000,000,000)
for _ in range(Q):
    p = int(input().strip())
    l = bisect_left(p)

    if l == N: # 1 - (N-1) 범위를 벗어났다 -> p 이상인 사과가 없다
        print(0)
    else:
        print(count[l])