import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

shape = 'IOI'
left = 0
cnt = 0
ans = 0
while left < m - len(shape) + 1:
    if s[left: left + len(shape)] == shape:
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
        
        left += 1
    else:
        cnt = 0
    
    left += 1

print(ans)