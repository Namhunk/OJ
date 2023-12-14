import sys

e, s ,m = map(int, sys.stdin.readline().strip().split())

if (e*532*13+s*285*17+m*420*10)%7980 == 0: print(7980)
else:print((e*532*13+s*285*17+m*420*10)%7980)