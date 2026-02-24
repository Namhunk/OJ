import sys
input = sys.stdin.readline

def solve():
    # Test Case의 개수 TC
    TC = int(input().strip())

    # 1000 이하의 모든 삼각함수를 구함
    T = [1, 3]
    while T[-1] < 1000:
        num = T[-1] * 2 - T[-2] + 1
        T.append(num)

    T_SUM = set() # 3개의 합을 모두 구해 저장한 집합
    
    for i in T:
        for j in T:
            for k in T:
                T_SUM.add(i+j+k)

    for _ in range(TC):
        # 자연수 K (3 <= K <= 1,000)
        K = int(input().strip())
        if K in T_SUM: print(1)
        else: print(0)

if __name__ == '__main__':
    solve()

"""
자연수가 주어졌을 때 그 정수가 3개의 삼각함수로 표현될 수 있는지
표현될 수 있다면 1, 없다면 0


삼각함수는 
1, 3, 6, 10, 15, 21

현재 삼각함수가 arr[i] 라면 arr[i-1] + (arr[i-1] - arr[i-2]+1)
2 x arr[i-1] - arr[i-2] + 1로 표현할 수 있음

arr[i] + arr[j] + arr[k] (0 <= i <= j <= k <= len(arr))

전체 arr의 크기는 45개이므로 전체를 사용해도 괜찮을것으로 보임

"""