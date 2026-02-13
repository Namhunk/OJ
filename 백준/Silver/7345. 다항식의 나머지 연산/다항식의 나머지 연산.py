import sys
input = sys.stdin.readline

"""
1. 두 다항식을 더함
2. 결과에 각 계수들에 대해 2로 나눈 나머지를 각각 대입


계수가 0 또는 1로만 이루어지는 다항식들의 집합에 대해 
d(최고차수)+1, 각 자리수들의 계수

다항식의 차수는 1000보다 작음
"""

def calculate(f, g, h):
    n = f[0]
    m = g[0]
    fg_size = n + m - 1
    fg = [0] * fg_size
    
    for i in range(1, n + 1):
        if f[i] == 0: continue
        for j in range(1, m + 1):
            fg[(i-1) + (j-1)] ^= (f[i] * g[j])
            
    h_len = h[0]
    
    for i in range(fg_size - h_len + 1):
        if fg[i] == 1:
            for j in range(h_len):
                fg[i + j] ^= h[j + 1]

    start = 0
    while start < len(fg) and fg[start] == 0:
        start += 1
    
    if start == len(fg):
        return [1, 0]
    
    remainder = fg[start:]
    return [len(remainder)] + remainder


# 테스트 케이스 수
T = int(input().strip())
for _ in range(T):
    # 0번 idx를 제외한 나머지는 각 항들의 계수(내림차순)
    f = list(map(int, input().strip().split()))
    g = list(map(int, input().strip().split()))
    h = list(map(int, input().strip().split()))

    ans = calculate(f, g, h)
    print(*ans)