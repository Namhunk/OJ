import sys

n = int(sys.stdin.readline().strip())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

white, blue = 0, 0

def check(x, y, n):
    global white, blue
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                check(x, y, n//2)
                check(x, y+n//2, n//2)
                check(x+n//2, y, n//2)
                check(x+n//2, y+n//2, n//2)
                return 
            
    if not color: white += 1
    else: blue += 1

check(0, 0, n)
print(white, blue)