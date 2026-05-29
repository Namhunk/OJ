def solution(land, P, Q):
    
    # 1차원으로 변경 후 정렬
    arr = []
    for row in land:
        arr.extend(row)
    arr.sort()
    
    n = len(arr)
    add = 0 # 추가
    rem = sum(arr)-(arr[0]*n) # 제거
    
    answer = add*P + rem*Q
    for i in range(1, n):
        if arr[i-1] == arr[i]: continue # 이전 값과 다른 경우
        
        diff = arr[i] - arr[i-1]
        
        add += diff * i # 현재 위치 이전 까지 추가
        rem -= diff * (n-i) # 나머지 제거
        
        curr = add*P + rem*Q
        
        if curr > answer: break
        
        answer = curr
        
    return answer