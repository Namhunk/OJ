import sys
input = sys.stdin.readline

# L보다 크거나 같고, U보다 작거나 같은 모든 정수의 각 자리의 합을 구해라

# L, U 입력 0 <= L <= U <= 2,000,000,000
L, U = input().strip().split()
L = '0' if L == '0' else str(int(L)-1)

arr = [[0]*10 for _ in range(len(U)+1)] # 합을 저장할 배열
nums = [0] * (len(U)+1) # 각 자라수의 합

for i in range(10): # 1자리 숫자 입력
    arr[0][i] = i

nums[1] = 45 # 1자리 숫자의 총 합

for i in range(1, len(U)+1): # 두 자릿수 부터 전체 길이
    nums[i] = (nums[i-1] * 10) + 45 * (10 ** (i-1)) # 다음 합을 계산하기 위한 총합

    for j in range(10):
        arr[i-1][j] = nums[i-1] + j * (10 ** (i-1)) # 이전 합 + 현재 숫자 등장 횟수

def calc(S, arr):
    l = len(S) # 현재 숫자의 길이
    pre = 0 # 지금까지 지나온 숫자들의 누적 자릿수 합
    res = 0 # 최종 결과값

    for i in range(l):
        dec = int(S[i]) # 현재 자릿수 값
        for j in range(dec):
            res += arr[l-i-1][j] + pre * (10 ** (l - i - 1))

        pre += dec

    return res + pre

ans = calc(U, arr) - calc(L, arr)
print(ans)