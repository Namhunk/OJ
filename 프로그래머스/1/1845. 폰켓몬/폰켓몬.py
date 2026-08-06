# 1 <= nums <= 10,000
# 1 <= nums[i] <= 200,000

def solution(nums):
    n = len(nums)
    
    cnt = len(set(nums))
    
    answer = min(n/2, cnt)
    return answer

'''
N/2 마리의 폰켓몬을 선택하는 방법 중
가장 많은 종류 번호의 개수를 return

각 폰켓몬 종류에 따라 번호가 다름

집합 <= n/2 를 만족하는 개수

'''