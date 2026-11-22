import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    p = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    arr = eval(sys.stdin.readline().strip())
    
    flip = 0
    s, e = 0, n
    if p.count('D') > n:
        print('error')
    else:
        for func in p:
            if func == 'R':
                flip = (flip + 1) % 2
            else:
                if flip: e-= 1
                else: s += 1
        
        arr = arr[s:e]

        if flip: print("".join(list(str(arr[::-1]).split())))
        else: print("".join(str(arr).split()))