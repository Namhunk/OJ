import sys

for _ in range(int(sys.stdin.readline().strip())):
    dic = {}
    for _ in range(int(sys.stdin.readline().strip())):
        name, clothes = sys.stdin.readline().strip().split()
        if clothes not in dic.keys(): dic[clothes] = 2
        else: dic[clothes] += 1
    
    if len(dic) != 0:
        k = 1
        for i in dic.values():
            k *= i
        
        print(k-1)
    else:
        print(0)