import sys

w = 0
s = 0

for i in range(1, 6):
    s_list = list(map(int, sys.stdin.readline().strip().split()))
    if sum(s_list) > s: s = sum(s_list); w = i

print(w, s)