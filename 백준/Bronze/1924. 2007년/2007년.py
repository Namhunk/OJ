import sys

mm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

m, d = map(int, sys.stdin.readline().strip().split())

s = 0

for i in range(m-1):
    s += mm[i]

s += d

print(week[s%7])