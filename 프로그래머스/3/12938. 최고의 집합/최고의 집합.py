# 1 <= n <= 10,000
# 1 <= s <= 100,000,000
def solution(n, s):
    arr = [s//n for _ in range(n)]
    SUM = sum(arr)
    R = [0, n] # +1을 할 범위
    for i in range(n+1):
        if SUM + n - i == s:
            R[0] = i
    
    for i in range(R[0], R[1]): # R 범위의 값들에 + 1
        arr[i] += 1
    
    answer = []
    if arr[0] == 0: # 가장 작은 값이 0이라면 -1 반환(각 원소는 자연수)
        answer.append(-1)
    else:
        answer.extend(arr)
        
    return answer

"""
자연수 n개로 이루어진 중복 집합은 다음 조건을 만족
1. 각 원소의 합이 S
2. 위 조건을 만족하며 각 원소의 곱이 최대

------------------------------------------
최고의 집합을 찾으려면
만약 n = 2, s = 10인 경우

l x r
-----
1 x 9
2 x 8
3 x 7
4 x 6
5 x 5

l = 5, r = 5 일때 곱이 가장 큼
그러면 i = 0 1, ..  n-1 까지, 길이가 n인 배열은
arr[0] <= arr[1] <= .. <= arr[i] <= .. <= arr[n-1] 를 만족 해야 함
arr[0] + arr[1] + .. arr[i] + .. arr[n-1] = s 가 되어야 함

길이 n의 배열 arr에 s//n으로 값들을 채워줌
arr = [s//n, s//n, ... s//n], len(arr) = n

반복문으로 0 부터 n-1 까지 돌면서(i = 0, 1, .. n)
현재 합이 SUM = s//n * n일때
SUM < s 인 동안
i 부터 n-1의 값들에 + 1을 해줌
a = s//n 일때
SUM - (a * (n-i) + (a+1) * (n-i)) == s
식을 전개

SUM - an + ai + an - ai + n  - i == s
SUM + n - i == s
an + n - i == s


"""