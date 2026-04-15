import sys
input = sys.stdin.readline

def find(x):
    if x != arr[x]: arr[x] = find(arr[x])

    return arr[x]

def union(x, y):
    x, y = find(x), find(y)
    if x < y: x, y = y, x
    arr[x] = y

def solve(I):
    global arr
    # N (1 <= N <= 10^6)
    N = int(input().strip())

    arr = [i for i in range(N)]

    # 1 <= K <= 10^5
    K = int(input().strip())
    for _ in range(K):
        a, b = map(int, input().strip().split())

        if find(a) != find(b):
            union(a, b)
    
    M = int(input().strip())
    print(f'Scenario {I}:')
    for _ in range(M):
        u, v = map(int, input().strip().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    
    print()
    
if __name__ == '__main__':
    T = int(input().strip())
    for I in range(1, T+1):
        solve(I)

"""

"""