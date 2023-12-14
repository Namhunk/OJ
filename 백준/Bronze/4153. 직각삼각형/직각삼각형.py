while True:
    sidelist = list(map(int, input().split()))
    if sum(sidelist) == 0: break
    sidemax = max(sidelist)
    sidelist.remove(sidemax)
    if sidemax ** 2 == sidelist[0] ** 2 + sidelist[1] ** 2: print("right")
    else: print("wrong")

