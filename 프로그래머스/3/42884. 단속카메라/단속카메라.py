# 1 <= len(routes) <= 10,000
# | routes[i] | <= 30,000

def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    before = -float('inf')
    answer = 0
    for s, e in routes:
        if s > before:
            answer += 1
            before = e
            
    return answer

"""
고속도로를 이동하려는 차량의 경로 routes가 주어질 때
모든 차량이 한 번은 단속용 카메라를 만나게 하려면 최소 몇 대를 설치해야 하는지

routes[i][0] i번째 차량이 고속도로에 진입한 지점
routes[i][1] i번째 차량이 고속도로에서 나간 지점

나간 지점들로 정렬해서

만약 현재 시작 지점이 이전 종료 지점보다 작거나 같다면 유지
크다면 + 1을 해주는게 좋아 보임
"""