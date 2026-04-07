import sys
input = sys.stdin.readline

def solve():
    # N (1 <= N <= 2,000)
    N = int(input().strip())

    arr = list(map(int, input().strip().split()))
    ans = []
    # 가장 긴 부분수열

    cnt = 0
    for i in range(N): # 모든 값들을 검사
        if not len(ans) or ans[-1] > arr[i]: # ans 배열에 값이 없거나 이전값이 현재값 보다 큰 경우
            ans.append(arr[i])
        else:
            l, r = 0, len(ans)-1
            while l < r:
                m = (l + r) // 2
                if ans[m] > arr[i]: l = m + 1
                else: r = m

            ans[l] = arr[i]
            cnt += 1
    
    print(cnt)

if __name__ == '__main__':
    solve()

"""
N명의 병사가 존재
각 병사는 특정 전투력을 보유, 병사를 배치할 때 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치

예제
1   2   3   4   5   6   7
15  11  4   8   5   2   4

15  11  8   5   4


"""