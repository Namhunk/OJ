import sys
num = set(2 * i + 1 for i in range(1, 500))
num.add(2)
for i in range(2, 32):
    inum = set(i * j for j in range(2, 1000//i + 1))
    num = num - inum

N = int(sys.stdin.readline().strip())
input_num = list(map(int, sys.stdin.readline().strip().split()))
count = 0
for i in range(N):
    if input_num[i] > 0 and input_num[i] in num:
        count += 1
print(count)