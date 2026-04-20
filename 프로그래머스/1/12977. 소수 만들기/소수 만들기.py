def solution(nums):
    P = [False]*2 + [True]*2999
    for i in range(2, int(len(P)**0.5)+1):
        if not P[i]: continue
        for j in range(i*2, len(P), i):
            if not P[j]: continue
            P[j] = False
    
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                SUM = nums[i] + nums[j] + nums[k]
                if not P[SUM]: continue
                answer += 1

    return answer