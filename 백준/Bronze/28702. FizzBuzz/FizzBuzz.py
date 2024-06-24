import sys

# i가 3의 배수 = 3
# i가 5의 배수 = 5

# if 3 & 5 -> "FizzBuzz"
# if 3 & not 5 -> "Fizz"
# if not 3 & 5 -> "Buzz"
# if not 3 & not 5 -> i

# 세 문자열 다음에 올 문자열을 출력(입력은 항상 연속된 문자열)
# 연속된 3개의 문자열중 1개는 i가 들어가야 한다면?
arr = list(sys.stdin.readline().strip() for _ in range(3))

ans = 0
for i in range(3):
    if arr[i].isnumeric(): ans = int(arr[i]) + (3-i); break

if not ans % 15: print('FizzBuzz')
elif not ans % 5: print('Buzz')
elif not ans % 3: print('Fizz')
else: print(ans)