import sys

c = int(sys.stdin.readline().strip())
for _ in range(c):
    n, score = sys.stdin.readline().strip().split(maxsplit=1)
    score_list = list(map(int, score.split()))
    avg = sum(score_list) / int(n)

    ans = list(filter(lambda x : x > avg, score_list))
    print(f'{round(len(ans) /int(n) * 100, 3):.3f}%')