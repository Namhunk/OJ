import sys
import re
input = sys.stdin.readline
T = int(input().strip())
for _ in range(T):
    string = input().strip()
    ans = re.compile('(100+1+|01)+')

    if ans.fullmatch(string):
        print('YES')
    else:
        print('NO')