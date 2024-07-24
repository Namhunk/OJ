import sys
input = sys.stdin.readline

# 2차원 평면상에 N개의 점으로 이루어진 다각형의 면적을 구해라

# N(3 <= N <= 10,000)
N = int(input().strip())
# 좌표값 x, y / 좌표값은 절대값 100,000을 넘지 않는다
x_point = []
y_point = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    x_point.append(x)
    y_point.append(y)

x_point.append(x_point[0])
y_point.append(y_point[0])

# 첫째 줄에 면적을 출력, 면적을 출력할 떚는 소수점 아래 둘쨰 자리에서 반올림하여 첫째 자리까지 출력
# 외적을 사용

left, right = 0, 0
for i in range(N):
    left += (x_point[i]*y_point[i+1])
    right += (y_point[i]*x_point[i+1])

ans = abs(left - right)/2
print(ans)