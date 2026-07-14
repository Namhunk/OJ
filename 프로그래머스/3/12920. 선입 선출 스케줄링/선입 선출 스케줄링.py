def solution(n, cores):
    m = len(cores)
    
    # 작업 수가 코어 수보다 적거나 같으면
    if n <= m:
        return n  # 앞에서 n번째 코어가 마지막 작업

    # 처음 한 번씩 할당된 m개의 작업 제거
    n -= m  
    
    left, right = 1, max(cores) * n

    # 남은 n개의 작업을 처리하는 데 필요한 최소 시간 T 찾기
    while left < right:
        mid = (left + right) // 2

        processed = 0
        for c in cores:
            processed += mid // c

        if processed >= n:
            right = mid
        else:
            left = mid + 1

    T = left

    # T-1초까지 처리된 작업 수를 빼서,
    # T초에 새로 시작해야 할 남은 작업 수를 구한다.
    remain = n
    for c in cores:
        remain -= (T - 1) // c

    # T초에 작업을 새로 시작하는 코어를 앞에서부터 확인
    for i, c in enumerate(cores):
        if T % c == 0:
            remain -= 1
            if remain == 0:
                return i + 1  # 1-index
'''
n개의 작업, 각 처리시간 cores 가 주어질 때
마지막 작업을 처리하는 코어의 번호를 return

1. 각 코어는 작업이 끝나면 다음 작업을 받음
2. 2개 이상의 코어가 동시에 끝나면 앞에서부터 받음
------------------------------------------------------

1. 앞에서부터 작업을 받음
2. n <= len(cores) 라면 n개의 코어들 중 처리 시간이 가장 긴 코어가 정답
3.  n > len(cores) 라면
'''