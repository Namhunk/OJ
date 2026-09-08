def solution(n):
    answer = 0
    arr = [i for i in range(n+1)]
    
    cur = n
    i = 1
    while cur > 0:
        if cur % i == 0:
            answer += 1
        
        cur -= i
        i += 1
    
    return answer

'''
1 <= n <= 10,000 일때
연속된 자연수들로 n을 표현하는 방법의 수
-----------------------------------

1. n을 만들 수 있는 연속된 자연수는 n이하 숫자임

시작값이 a라고 할때 n은

(a + 0) + (a + 1) + (a + 2) + (a + 3) + .. + (a + (i-1)) = n

a*i + i(i-1) / 2 = n
a*i = n - i(i-1) / 2
a = (n - i(i-1)/2) / i

a는 자연수
1 ~ (i-1) 까지의 합을 K라 할때
n-k / i 가 자연수가 되어야만 성립이 가능


'''