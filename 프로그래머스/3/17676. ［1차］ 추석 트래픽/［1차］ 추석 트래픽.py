# N = len(lines) (1 <= N <= 2,000)
def solution(lines):
    N = len(lines)
    arr = [] # 각 로그의 기록을 보고 시작, 종료, 처리 시간을 저장
    
    for i in range(N):
        log = lines[i].split()
        S = log[1]
        T = float(log[2].strip('s'))*1000 # 오른쪽 s 문자 제거
        
        # 전체 시간은 1분 = 60, 1시 = 60*60
        # 01:00:04.001 = 1*60**2 + 0*60 + 4 + 0.001
        time = list(map(float, S.split(':')))
        
        end = 0
        for j in range(2, -1, -1):
            end += time[2-j]*(60**j)*1000
        
        start = end - T + 1
        
        arr.append((start, end, T))
    
    arr.sort(key=lambda x: x[0]) # 시작시간이 작은 순
    
    answer = 0
    for i in range(N):
        s, e, _ = arr[i]
        ws = s
        we = s + 999
        cnt = 0
        for j in range(N):
            ts, te, _ = arr[j]
            if ws <= te and ts <= we:
                cnt += 1
        
        answer = max(answer, cnt)
        
        ws = e
        we = e + 999
        cnt = 0
        for j in range(N):
            ts, te, _ = arr[j]
            if ws <= te and ts <= we:
                cnt += 1
        
        answer = max(answer, cnt)
    return answer

"""
lines에는 응답 완료시간 S, 처리시간 T가 주어짐

초당 최대 처리량을 계산
초당 최대 처리량은 요청의 응답 완료 여부에 관계없이
임의 시간부터 1초(1000밀리초)간 처리하는 요청의 최대 개수

-----------------------------------

겹치는 구간의 최대 개수
종료 기준 시점이어야 하므로

lines의 크기는 최대 2,000
시작까지 포함한다면 4,000

2016-09-15의 00:00시 부터
2016-09-16까지


01:00:02.003 - 01:00:04.002
01:00:05.001 - 01:00:07.000
각 구간을 1초로 나눴을 때

04.001 - 05.001 초에서 2개가 겹침
--------------------------------------
1. 각 시간을 정렬
"""