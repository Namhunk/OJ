import sys
input = sys.stdin.readline

from heapq import heappush, heappop
def solve():
    # N (1 <= N <= 200,000)
    N = int(input().strip())

    # (0 <= S[i] < T[i] <= 10**9)
    ST = []
    for _ in range(N):
        ST.append(list(map(int, input().strip().split())))
    
    ST = sorted(ST)
    heap = [ST[0][1]]
    for i in range(1, N):
        if heap[0] <= ST[i][0]:
            heappop(heap)
        
        heappush(heap, ST[i][1])
    
    print(len(heap))

if __name__ == '__main__':
    solve()

"""
S[i]에 시작해서 T[i]에 끝나는 N개의 수업
최소 개수의 강의실을 사용해 모든 수업을 끝내야 함


1. 현재 i번째 수업에서 필요한 정보는 이전 수업들의 종료 시점
    S[i] >= T[i-1], T[i-2], .. 를 만족한다면 개수를 늘리지 않아도 됨



"""