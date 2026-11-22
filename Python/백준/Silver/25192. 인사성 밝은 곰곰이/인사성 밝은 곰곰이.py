import sys

n = int(sys.stdin.readline().strip())

ENTER_CNT = 0
Dict = {}
for _ in range(n):
    string = sys.stdin.readline().strip()

    if string == "ENTER": ENTER_CNT += 1; Dict[ENTER_CNT] = set()
    else:
        Dict[ENTER_CNT].add(string)

ans = 0
for i in range(1, ENTER_CNT+1):
    ans += len(Dict[i])

print(ans)