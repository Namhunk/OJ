import sys
input = sys.stdin.readline

"""
각 테스트 케이스에 대해 정화의 방패를 완성하는 세 별빛 수정의 마력 a,b,c와
두 마법 룬에 해당하는 부호를 공백으로 구분해 출력

(a, b, c) >= 1

k 값은 a, b, c의 각 제곱의 합 또는 차로 구할 수 있음
각 a, b, c는 고유한 1 이상의 정수 
"""
"""
a**2 = A, b**2 = B, c**2 = C라고 할 때
A + B + C = x
A - B - C = y
A + B - C = z
A - B + C = w
x, y, z, w 중 1가지는 k값이어야 함
이때 모든 식을 더하면
4A = x+y+z+w 가 나옴 x, y, z, w중 하나의 값을 k라고 할 때
4A = k + x + y + z 로 바꿀 수 있음 이때 2A와 x, y, z, k중 두 변수의 합은 같음 y+z를 2A라 하면
2A + 2A = k + x + (y+z) = k + x + 2A
2A = k+x
이때 우리는 k값을 알고 있음
k = 3이라 할 때
2A = x + 3
A = (x + 3) / 2
a**2 = (x + 3) / 2
(x+3)의 값은 짝수 and 제곱수를 만족 해야함
이때 들어올 수 있는 값들은 5, 15, 29, 47, 69, 95, ... 등이 있음
A > B > C라고 한다면 A는 최소 9보다 커야함

또한 | A - k | = | B + C | or | B - C|를 만족해야함

"""
import math
def solve(k):
    start = math.isqrt(k)
    i = 0
    while True:
        m_high = start + i
        A = m_high * m_high
        target = A - k
        if target > 0:
            limit = math.isqrt(target // 2)
            for b in range(1, limit + 1):
                c_sq = target - b * b
                c = math.isqrt(c_sq)
                if c * c == c_sq and c > 0:
                    if m_high != b and b != c and m_high != c:
                        return f'{m_high} - {b} - {c}'
        m_low = start - i
        if m_low > 0:
            A = m_low * m_low
            target = k - A
            if target > 0:
                limit = math.isqrt(target // 2)
                for b in range(1, limit + 1):
                    c_sq = target - b * b
                    c = math.isqrt(c_sq)
                    if c * c == c_sq and c > 0:
                        if m_low != b and b != c and m_low != c:
                            return f'{m_low} + {b} + {c}'

        if i >= 1:
            c = i
            target_plus = k + c * c
            limit_search = math.isqrt(target_plus // 2)
            for a in range(1, limit_search + 1):
                b_sq = target_plus - a * a
                b = math.isqrt(b_sq)
                if b * b == b_sq:
                     if a != b and b != c and a != c:
                        return f'{a} + {b} - {c}'

        i += 1


# 테스트 케이스 수 T (1 <= T <= 1000)
T = int(input().strip())

for _ in range(T):
    k = int(input().strip()) # (1 <= K <= 1e9)
    print(solve(k))
