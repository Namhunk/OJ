import sys

# 5x10^6, 2x li^t
for _ in range(int(sys.stdin.readline())):
    li = []

    while len(li) < 41:
        l = int(sys.stdin.readline().strip())
        if l == 0: break

        li.append(l)
    
    li.sort(reverse= True)
    r = 0

    for i in range(1, len(li)+1):
        r += 2*(li[i-1]**i)
    
    print(r if r < 5*(10**6) else "Too expensive")