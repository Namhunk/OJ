def solution(play_time, adv_time, logs):
    play = to_sec(play_time)
    adv  = to_sec(adv_time)
    
    arr = [0]*(play+1)
    
    for log in logs:
        s, e = log.split('-')
        st = to_sec(s)
        et = to_sec(e)
        
        arr[st] += 1
        if et <= play:
            arr[et] -= 1
    
    for i in range(1, play + 1): # 시청자 수
        arr[i] += arr[i - 1]
    
    for i in range(1, play + 1): # 누적 시간
        arr[i] += arr[i - 1]
        
    max_time = arr[adv - 1]
    answer = 0
    
    for start in range(1, play - adv + 1):
        end = start + adv - 1
        cur = arr[end] - arr[start - 1]
        
        if cur > max_time:
            max_time = cur
            answer = start
    
    return to_time(answer)
    
    answer = ''
    return answer

def to_sec(time): # 시간 -> 초
    h, m, s = map(int, time.split(':'))
    return h*3600 + m*60 + s

def to_time(sec): # 초 -> 시간
    h = sec // 3600
    sec %= 3600
    
    m = sec // 60
    s = sec % 60
    
    return f'{h:02d}:{m:02d}:{s:02d}'
    
    
    

'''
누적 재생시간이 가장 많이 나오는 곳에 광고를 삽입

최대 99H, 59M, 59S 까지 가능

배열 최대 길이 360,000

전체 누적합 배열을 생성 후

첫 누적은 시청자 수
두번째 누적은 시청자 기반 누적 시간

각 시작부터 광고 길이 사이까지
'''