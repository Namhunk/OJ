# 1 <= len(cookie) <=   2,000
# 1 <= cookie[i] <= 500
def solution(cookie):
    N = len(cookie)
    arr = [0]*(N+1)
    
    answer = 0
    for i in range(1, N+1):
        arr[i] += (arr[i-1] + cookie[i-1])
        
    for r in range(2, N+1):
        for l in range(r-1):
            if (arr[r]-arr[l]) % 2 == 1: continue
            s, e = l+1, r-1
            while s < e:
                m = (s + e) // 2
                
                left = arr[m] - arr[l]
                right = arr[r] - arr[m]
                
                if left < right:
                    s = m+1
                else:
                    e = m
            
            left_sum = arr[s]-arr[l]
            right_sum = arr[r]-arr[s]
            if left_sum == right_sum:
                answer = max(answer, left_sum)
                
    return answer

"""
각 원소는 바구니, 숫자는 과자의 개수

- 배열이 주어졌을 때 start, end 범위를 지정하고 m으로 나눔
- m을 기준으로 나눴을 때 과자의 개수가 같아야 함
- 최대한 많은 과자 수 return

-----------------------------------------------------------
l, m, r 을 이동 가능
arr[m] - arr[l] == arr[r]-arr[m]

r은 계속 증가
l은 r-1보다 작아야 함
"""