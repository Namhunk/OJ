def solution(sequence, k):
    n = len(sequence)
    answer = [-1, -1]
    
    # 2. l = 0, r = 1 위치부터 k보다 작으면 r증가
    # 크면 l증가로 탐색, 길이가 이전보다 작은 경우만
    
    l = 0
    size = float('inf')
    curr = 0
    for r in range(n):
        curr += sequence[r]
        
        while l < r and curr > k:
            curr -= sequence[l]
            l += 1
        
        if curr == k and r-l+1 < size:
            size = r-l+1
            answer[0] = l
            answer[1] = r
        
    return answer

'''
다음 조건을 만족하는 부분수열을 찾아라
1. 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함
2. 부분 수열의 합은 K
3. 합이 K인 부분 수열이 여러개인 경우 가장 짧은것
4. 길이가 짧은게 여러개인 경우 인덱스가 가장 작은것

부분수열의 시작 인덱스와 마지막 인덱스를 배열에 담아
return


'''