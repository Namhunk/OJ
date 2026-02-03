import sys

# 빠른 입출력을 위한 설정
input = sys.stdin.readline

def solve():
    try:
        # 입력 파싱
        # 첫 줄 N
        line1 = input().split()
        if not line1: return # 입력이 없는 경우 처리
        N = int(line1[0])
        
        finite_items = []   # 탈 때마다 재미가 주는 놀이기구 (개별 아이템으로 분리)
        infinite_items = [] # 재미가 안 주는 놀이기구
        
        for _ in range(N):
            a, b, t = map(int, input().split())
            
            if b > 0:
                # 재미가 양수일 때까지만 아이템 생성
                k = 1
                while True:
                    fun = a - (k-1)**2 * b
                    if fun <= 0:
                        break
                    finite_items.append((t, fun))
                    k += 1
            else:
                # b=0이면 재미가 일정함 (무한 아이템)
                if a > 0:
                    infinite_items.append((t, a))
        
        # 쿼리 수와 시간들 읽기
        Q = int(input())
        queries = []
        for _ in range(Q):
            queries.append(int(input()))
            
        # 최대 시간 계산 (쿼리 중 가장 큰 값 혹은 25000)
        # 문제 조건상 T <= 25000이므로 25000까지 잡아도 됨
        MAX_TIME = 25000
        dp = [0] * (MAX_TIME + 1)
        
        # 1. 유한 아이템 처리 (0/1 Knapsack) - 뒤에서부터 갱신
        for cost, val in finite_items:
            for j in range(MAX_TIME, cost - 1, -1):
                if dp[j - cost] + val > dp[j]:
                    dp[j] = dp[j - cost] + val
                    
        # 2. 무한 아이템 처리 (Unbounded Knapsack) - 앞에서부터 갱신
        for cost, val in infinite_items:
            for j in range(cost, MAX_TIME + 1):
                if dp[j - cost] + val > dp[j]:
                    dp[j] = dp[j - cost] + val
        
        # 3. 시간 T보다 적게 썼을 때가 더 이득일 수 있으므로 Prefix Max 처리
        # (사실 위 로직에서 0으로 초기화하고 max갱신하므로 빈 공간은 0이지만,
        #  시간을 꽉 채우지 않아도 되는 경우를 위해 앞의 최댓값을 가져옴)
        for i in range(1, MAX_TIME + 1):
            if dp[i-1] > dp[i]:
                dp[i] = dp[i-1]
                
        # 결과 출력
        for t in queries:
            # 쿼리 시간이 25000을 넘을 수도 있는지 체크(문제엔 25000이하라 했으나 안전하게)
            t = min(t, MAX_TIME)
            print(dp[t])
            
    except Exception:
        return

if __name__ == '__main__':
    solve()
