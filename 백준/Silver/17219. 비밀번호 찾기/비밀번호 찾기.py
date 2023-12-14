import sys

n, m = map(int, sys.stdin.readline().strip().split())
dict = {}
for _ in range(n):
    url, pwd = sys.stdin.readline().strip().split()
    dict[url] = pwd

for _ in range(m):
    find = sys.stdin.readline().strip()
    print(dict[find])

    