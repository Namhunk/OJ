import sys

# + : 두 문자열을 이어 붙임, - : 양쪽 문자열을 수로 해석 후 빼기
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
C = sys.stdin.readline().strip()

# 첫 줄 (숫자) -> A + B - C
# 둘째 줄 (문자열) -> A + B - C

print(int(A) + int(B) - int(C))
print(int(A+B) - int(C))