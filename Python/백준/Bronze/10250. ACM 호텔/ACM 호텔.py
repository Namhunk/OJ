for _ in range(int(input())):
    H, W, N = map(int, input().split())
    Hotel = [[(j + i) for i in range(1, W + 1)] for j in range(100, H * 100 + 1, 100)]
    print(Hotel[H - 1 if N % H == 0 else N % H - 1][N // H if N % H > 0 else N // H - 1])