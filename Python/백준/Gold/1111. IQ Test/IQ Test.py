import sys
input = sys.stdin.readline

def solve(N, arr):
    if N < 2: # 숫자 1개인 경우
        return 'A'
    else:
        if arr.count(arr[0]) == N: # 같은 값
            return arr[0]
        else:
            if N < 3: # 숫자 2개 + 다른 값
                return 'A'
            else: # 숫자 3개 이상
                if (arr[1] - arr[0]) == 0:
                    return 'B'
                a = (arr[2] - arr[1]) / (arr[1] - arr[0])
                b = arr[1] - arr[0]*a

                if int(a) != a or int(b) != b: # a, b 정수 아님
                    return 'B'

                flag = 1
                cur = arr[0]*a + b
                for i in range(1, N):
                    if arr[i] != cur:
                        flag = 0
                        break

                    cur = arr[i]*a + b

                if not flag:
                    return 'B'
                else:
                    return int(arr[-1]*a+b)

def main():
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(solve(N, arr))
    
if __name__ == '__main__':
    main()