# 1 <= n <= 15
def solution(n):
    global answer
    answer = []
    
    hanoi(n, 1, 2, 3)
    return answer

def hanoi(n, start, via, end):
    global answer
    if n == 1:
        answer.append([start, end])
        return
    
    hanoi(n-1, start, end, via)
    answer.append([start, end])
    hanoi(n-1, via, start, end)

'''
n개의 원판을 3번 원판으로 옮기느 최소 횟수 return

1. 한 번에 하나의 원판만 옮김
2. 큰 원판이 작은 원판위에 있으면 안됨

----------------------------------------------------
- 기둥은 3개 고정
- 초기에는 1번 기둥에 n개의 원판이 올라갈수록 작게 정렬
- 원판을 현재 위치 -> 다음 위치 로 옮기면서 answer에 현재 기둥 -> 다음 기둥 을 숫자로 저장
'''