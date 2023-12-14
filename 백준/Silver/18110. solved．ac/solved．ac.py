import sys

n = int(sys.stdin.readline().strip())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
arr.sort()

cut = int(n * 0.15) + (1 if (n*0.15%1)*10 >= 5 else 0)
ans = 0

if not n: print(0)
else:
    ans = sum(arr[cut: n-cut]) / (n - cut*2)
    ans = int(ans) + (1 if (ans%1)*10 >= 5 else 0)
    print(ans)