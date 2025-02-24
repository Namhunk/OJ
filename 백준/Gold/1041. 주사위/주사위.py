import sys
input = sys.stdin.readline

# 보이는 5개의 면에 쓰여있는 수의 합의 최솟값을 출력

# 동일한 주사위를 N^3개 가지고 있을 때, 주사위를 적절히 회전시키고 쌓아서 NxNxN크기의 정육면체를 만든다

# N(1 <= N <= 1,000,000)
N = int(input().strip())

# 주사위의 숫자 (1 <= arr[i] <= 50)
arr = list(map(int, input().strip().split())) # 주사위

if N == 1: # 주사위가 1개일 떄
    ans = sum(arr) - max(arr) # 가장 큰 숫자를 제외한 나머지 면의 합
    print(ans)
else: # 나머지 경우
    seq = [4, 0, 1, 5, 4] # E A B F E 순서

    case1 = float('inf') # 붙어있는 2개의 면의 합의 최솟값
    for i in range(len(seq)-1):
        case1 = min(case1, arr[seq[i]] + arr[seq[i+1]])

    case1 += min(arr[2], arr[3]) # C, D 중 작은 면
    case1 *= 4
    # cnt = (N-1)*4 + (N-2)*4
    case2 = float('inf')
    exc = {(0, 5), (2, 3), (4, 1)} # 제외할 쌍 (A, F), (C, D), (B, E)
    for i in range(6):
        for j in range(i+1, 6):
            if (i, j) not in exc and (j, i) not in exc:
                case2 = min(case2, arr[i] + arr[j])

    case2 *= ((N-1)*4 + (N-2)*4)
    case3 = min(arr) * ((N-2) * (N-1)*4 + (N-2)*(N-2))

    ans = case1 + case2 + case3
    print(ans)

"""
주사위는
    D
E   A   B   F
    C
    
    3
4   0   1   5
    2
의 형태

if N <= 1:
    1개의 면을 제외한 나머지
else:
    4개의 주사위는 3개의 면
    모서리 위치의 주사위는 2개의 면
    나머지는 1개의 면을 보여줌

각 변의 길이는 N
처음 4개는 arr[0, 1, 4, 5]에서 2개의 면씩 묶었을때 작은 2개 and arr[2, 3]중 작은 1개
다음 (N-1) * 4 + (N-2) * 4 개는 가장 작은 2개
나머지 (N-2) * (N-1) * 4 + (N-2) * (N-2)개는 1개
"""