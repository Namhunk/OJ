n,b,a = map(int,input().split())

price = list(map(int,input().split()))

price.sort()

answer = n

for i in range(n):
    
    b -= price[i]//2

    if i >= a:
        
        b -= price[i-a]//2
    
    if b < 0:
        
        answer = i
        
        break

print(answer)