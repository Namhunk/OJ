# 0 <= n <= 10
# 0 <= t <= 60
# 0 <= m <= 45
def solution(n, t, m, timetable):
    arr = []
    for time in timetable:
        hour, minute = map(int, time.split(':'))
        arr.append(hour*60 + minute) # 0부터 23*60+59 사이의 정수로 표현
    
    arr.sort()
    
    
    bus_times = [9*60 + i*t for i in range(n)] # 버스 도착 시간
    idx = 0
    last = []
    
    for bus_idx, bus in enumerate(bus_times):
        cnt = 0
        while idx < len(arr) and arr[idx] <= bus and cnt < m:
            if bus_idx == n-1:
                last.append(arr[idx])
            
            idx += 1
            cnt += 1
        
        if bus_idx != n-1:
            last = []
        last_bus_time = bus_times[-1]
        
        if len(last) < m:
            con_time = last_bus_time
        else:
            con_time = last[-1] - 1 
    
    answer = f'{con_time//60:02d}:{con_time%60:02d}'
    return answer
        
        

"""
셔틀은 09:00부터 n회 t분 간격으로 역에 도착
하나의 셔틀에는 최대 m명이 탑승 가능

셔틀을 타고 사무실로 갈 수 있는 도착 시간 중 제일 늦은 시각

n: 셔틀 운행 횟수
t: 셔틀 운행 간격
m: 한 셔틀에 탈 수 있는 최대 크루 수
timetable: 크루가 대기열에 도착하는 시각
"""