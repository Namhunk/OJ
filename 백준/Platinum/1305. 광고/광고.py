import sys
input = sys.stdin.readline

# 첫째 줄에 가능한 광고의 길이중 가장 짧은 것의 길이를 출력

# 광고판의 크기 L (1 <= L <= 1,000,000)
L = int(input().strip())

# 현재 광고판에 보이는 문자열
arr = list(input().strip())

def KMP_Table(arr):
    table = [0 for _ in range(len(arr))]

    i = 0
    for j in range(1, len(arr)):
        while i > 0 and arr[i] != arr[j]:
            i = table[i-1]

        if arr[i] == arr[j]:
            i += 1
            table[j] = i

    return i

pat = KMP_Table(arr)
print(L-pat)