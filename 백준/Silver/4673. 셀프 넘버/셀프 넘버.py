def d(n: int)->int:
    x = list(map(int, " ".join(str(n)).split()))
    s = n
    for i in x:
        s += i
    return s

def run(arr: list, s: int)-> None:
    print(s)
    while True:
        n = s
        s = d(n)
        if s >= len(arr): break
        arr[s] = False

self_nums = [False] + [True] * 10000

for i in range(1, 10001):
    if self_nums[i]:
        run(self_nums, i)