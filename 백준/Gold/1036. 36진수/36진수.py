import sys
input = sys.stdin.readline

# 가능한 합의 최댓값을 구하는 프로그램, 합의 최댓값도 36진수로 출력

# 36진수 한 자리 -> 10진수 값
def digit_to_val(num): # 0 - 9 값
    if '0' <= num <= '9':
        return ord(num) - ord('0')
    else: # A - Z 값
        return ord(num) - ord('A') + 10

# 10진수 값 -> 36진수 한 자리
def val_to_digit(val):
    if 0 <= val <= 9: # 0 - 9
        return chr(val+ord('0'))
    else:
        return chr(val-10+ord('A'))

# 10진수 정수 -> 36진수 문자열
def to_base36(num):
    if num == 0:
        return "0"

    digits = []
    while num > 0:
        digits.append(val_to_digit(num % 36))
        num //= 36

    return "".join(reversed(digits))

# 수의 개수 N
N = int(input().strip())

# N개의 수
arr = [input().strip() for _ in range(N)]

# 고를 숫자의 개수 K
K = int(input().strip())

# 모든 수를 10진수로 변환해 합을 구함
SUM = 0

# 각 숫자(문자)에 대해 Z로 치환했을 때 얻는 이득을 누적할 딕셔너리
gain_map = {}
for c in range(36):
    if c < 10:
        gain_map[chr(c+ord('0'))] = 0
    else:
        gain_map[chr(c-10+ord('A'))] = 0

for num in arr:
    for i in range(len(num)):
        digit = num[len(num) - 1 - i]
        val = digit_to_val(digit)
        SUM += val * (36 ** i)
        gain_map[digit] += (35 - val) * (36 ** i)

sorted_digits = sorted(gain_map.items(), key=lambda x: x[1], reverse=True)
sum_of_gains = sum(d[1] for d in sorted_digits[:K])
final_sum = SUM + sum_of_gains

print(to_base36(final_sum))
