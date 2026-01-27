import sys
input = sys.stdin.readline
"""
훼손된 숫자 *에 알맞는 숫자를 출력

일련번호 앞에서부터 각 자리마다 가중치 1, 3, 1, 3...를 곱한 것을 모두 더하고 10으로 나눴을 때
나머지가 0으로 만드는 m을 사용한다

*의 위치가 홀수번대 -> x1
*의 위치가 짝수번대 -> x3

(x + c) % 10 = 10-m

x % 10 = 10 - m - c%10

x % 10 = 10 - (m + c % 10)
"""

# 훼손번호 입력(체크기호를 제외한 무작위 한자리)
nums = list(input().strip())

total = 0
check = int(nums[12])
mul = 1
for i in range(12): # check 숫자를 제외한 나머지
    if (i+1) % 2 == 0:
        if nums[i] == '*': mul = 7; continue
        total += int(nums[i]) * 3
    else:
        if nums[i] == '*': mul = 1; continue
        total += int(nums[i])

ans = ((10 - (check+total%10)) * mul) % 10
print(ans)
