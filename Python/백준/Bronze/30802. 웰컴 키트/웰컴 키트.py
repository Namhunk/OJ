import sys
from math import ceil
# 티셔츠 사이즈 = S, M, L, XL, XXL, XXXL
# 펜은 한 종류, P자루씩 묶음으로 주문 or 한 자루씩 주문
# 티셔츠는 남아도 되지만 부족해선 안됨, 신처안 사이즈대로 나눠줘야함

N = int(sys.stdin.readline().strip())
Size = list(map(int, sys.stdin.readline().strip().split()))
T, P = map(int, sys.stdin.readline().strip().split())

# 첫 줄 : T장씩 최소 몇 묶음 주문해야 하는가
# 둘째 줄 : P자수씩 최대 몇 묶음 주문할 수 있는가, 그 때 펜을 한자루씩 몇개 주문하는가

Sum = sum(Size)
T_cnt = 0

for i in Size:
    T_cnt += ceil(i/T)

print(T_cnt)
print(Sum//P, Sum%P)