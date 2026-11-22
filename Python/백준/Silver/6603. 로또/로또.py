import sys
from itertools import combinations

while True:
    klotto = list(map(int, sys.stdin.readline().strip().split()))
    if len(klotto) == 1 and klotto[0] == 0: break

    k = klotto[0]
    lotto = klotto[1:len(klotto)]

    for i in combinations(lotto, 6):
        print(*i)
    
    print()