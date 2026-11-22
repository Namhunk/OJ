import sys
input = sys.stdin.readline

sentence = list(input().strip())

def KMP_Table(pattern):
    table = [0 for _ in range(len(pattern))]

    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table

ans = 0
for i in range(len(sentence)):
    ans = max(ans, max(KMP_Table(sentence[i:])))

print(ans)

