import sys
# 1 = 2초, 2 = 3초, 3 = 4초 ... 9 = 10초, 0 = 11초
word = ["", "", "", 'ABC','DEF', 'GHI', 'JKL', 'MNO','PQRS', 'TUV', 'WXYZ']
Time = 0

for i in sys.stdin.readline().strip():
    for j in range(len(word)):
        if i in word[j]: Time += j

print(Time)