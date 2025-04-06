import sys
input = sys.stdin.readline

# 첫째 줄에 집에 돌아오는데 걸리는 시간의 최솟값을 출력한다. 절대/상대 오차는 10^-9 까지 허용한다.

# 네 정수 X, Y, D, T
X, Y, D, T = map(int, input().strip().split())

dist = (X**2 + Y**2) ** 0.5

case1 = dist

jump = 0
cnt = 0

while jump <= dist:
    jump += D
    cnt += 1

cnt -= 1
jump -= D

case2 = max(T*(cnt+1), 2*T)
case3 = T*cnt + (dist-D*cnt)
case4 = T*(cnt+1)+(D*(cnt+1)-dist)

print(min(min(case1, case2), min(case3, case4)))