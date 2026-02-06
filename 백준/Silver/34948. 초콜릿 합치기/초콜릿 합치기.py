import sys
input = sys.stdin.readline

"""
초콜릿 중 몇개를 골라 합쳐야 함

초콜릿을 합치기 위해선, 사용할 초콜릿의 세로길이가 같아야 함,(세로 길이는 원하는 만큼 줄일 수 있음)
합친 후의 초콜릿 크기는 세로 x 가로 
"""
# 초콜릿 개수 N (1 <= N <= 200,000)
N = int(input().strip())

# 각 초콜릿의 세로길이를 나타내는 N개의 정수
H = list(map(int, input().strip().split()))

# 각 초콜릿의 가로 길이를 나타내는 N개의 정수
W = list(map(int, input().strip().split()))

# 높이와 너비를 묶어서 리스트로 만들고
# 높이를 기준으로 내림차순 정렬
chocolates = sorted(zip(H, W), key=lambda x: x[0], reverse=True) 

max_area = 0
curr_width_sum = 0

for h, w in chocolates:
    # 높이 더함
    curr_width_sum += w

    area = h * curr_width_sum

    if area > max_area:
        max_area = area
    
print(max_area)