import sys

fnums = [0, 1]

n = int(sys.stdin.readline().strip())

if n < 2: print(fnums[n])
else:
    for i in range(2, n+1):
        fnums.append(fnums[i-2]+fnums[i-1])
    print(fnums[-1])