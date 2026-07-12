# 1 <= e <= 5,000,000
# 1 <= len(start) <= min(e, 100,000)
# 1 <= start[i] <= e
def solution(e, starts):
    cnt = [1]*(e+1)
    for i in range(2, e+1): # 1부터 e까지 모든 숫자들에 대해
        for j in range(i, e+1, i):
            cnt[j] += 1
    
    nums = [i for i in range(e+1)] # 각 숫자들
    for i in range(e, 0, -1): # 역순으로
        if cnt[i] > cnt[i-1]:
            nums[i-1] = nums[i]
            cnt[i-1] = cnt[i]
    
    answer = []
    for s in starts:
        answer.append(nums[s])
    
    return answer

'''
1. 억억단에서 각 숫자가 등장하는 횟수를 구함
2. 주어진 범위 내에서 가장 많은 등장 횟수를 갖는 숫자를 찾음
3. 주어진 범위 내에서 등장 횟수의 최대가 같은 숫자가 여러개라면 그 중 가장 작은 값
------------------------------------------------------------
1. 각 숫자는 최소 1의 횟수를 가짐
2. 2부터는 각 배수들은 +1의 횟수를 가짐

2  4 6 8 10
'''