import sys
input = sys.stdin.readline

def solve():
    # 음의 개수 N (1 <= N <= 2x10**4), 고음의 첫 항과 공차 A, D (1 <= A, D <= 10**7)
    N, A, D = map(int, input().strip().split())

    # 참가자들의 음을 나타내는 N개의 정수가 순서대로 주어짐 (1 <= arr[i] <= 10**7)
    arr = list(map(int, input().strip().split()))
    
    ans = []
    for i in range(len(arr)):
        if arr[i] == A + D * len(ans):
            ans.append(arr[i])
    
    return len(ans)

if __name__ == '__main__':
    print(solve())



"""
음 A를 시작으로 D음씩 올라가는 X단 고음으로 가능한 가장 큰 X

현재 arr[i]에 대해 A를 시작으로 D음씩 올라가는 X단 고음 과정에 포함되어있는 숫자인지 확인

"""