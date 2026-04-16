import sys
input = sys.stdin.readline

def solve():
    a, b = input().strip().split()

    a_list = list(map(int, a[::-1]))
    b_list = list(map(int, b[::-1]))

    if len(a) <= len(b):
        ans = cal(a_list, b_list)
    else:
        ans = cal(b_list, a_list)
    
    print(ans)
    

def cal(a:list, b:list): # len(a) <= len(b)
    arr = []
    last = 0
    
    # 1. 먼저 더함
    for i in range(len(a)):
        arr.append(a[i] + b[i])
    
    for i in range(len(a), len(b)):
        arr.append(b[i])
    
    for i in range(len(arr)):
        if arr[i] >= 2:
            arr[i] = arr[i] % 2

            if i+1 < len(arr):
                arr[i+1] += 1
            else:
                arr.append(1)
    
    while len(arr)-1 and arr[-1] != 1:
        arr.pop()

    ans = ''.join(map(str, arr[::-1]))
    return ans

if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        solve()

"""
두 이진수가 주어졌을 때 그 합을 출력

"""