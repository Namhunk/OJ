import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_grade = {i:0 for i in range(1,6)}
seq_grade = {i:0 for i in range(1,6)}

for i in range(2):
    seq_grade[arr[0][i]] = 1
    max_grade[arr[0][i]] = 1
for i in range(1,N):
    if arr[i][0] == arr[i][1]:
        arr[i].pop()
    for num in arr[i]:
        seq_grade[num] += 1
        if num not in arr[i-1]:
            seq_grade[num] = 1
        max_grade[num] = max(max_grade[num],seq_grade[num])

max_cnt, max_num = 0, 0
for check in max_grade:
    if max_grade[check] > max_cnt:
        max_cnt = max_grade[check]
        max_num = check
print(max_cnt,max_num)
