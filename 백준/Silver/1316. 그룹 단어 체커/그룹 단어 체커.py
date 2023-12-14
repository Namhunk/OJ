import sys

count = 0

for _ in range(int(sys.stdin.readline().strip())):
    word = sys.stdin.readline().strip()
    insert = []
    tf = True
    for i in word:
        if i not in insert: insert.append(i)
        elif i != insert[-1]: tf = False; break

    if tf: count += 1

print(count)