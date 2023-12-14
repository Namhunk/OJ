fibo = [0, 1]
i = 1
while fibo[-1] < 1000000000:
    fibo.append(fibo[i-1] + fibo[i])
    i += 1

for _ in range(int(input().strip())):
    n = int(input().strip())
    l = []
    for i in range(len(fibo)-1, 1, -1):
        if fibo[i] <= n:
            l.append(fibo[i])
            n -= fibo[i]
        if n <= 0: break
    
    print(*l[::-1])