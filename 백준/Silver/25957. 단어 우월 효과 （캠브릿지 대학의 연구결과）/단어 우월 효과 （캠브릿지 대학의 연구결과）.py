import sys

n = int(sys.stdin.readline().strip())
Dict = {}
def match(word):
    key = word

    if len(word) > 2:
        key = "-".join([word[0], word[-1], "".join(sorted(word[1: -1]))])
    elif len(word) == 2:
        key = "-".join(list(word))
    
    return key

for _ in range(n):
    word = sys.stdin.readline().strip()
    
    Dict[match(word)] = word

m = int(sys.stdin.readline().strip())
arr = list(sys.stdin.readline().strip().split())

for i in arr:
    print(Dict[match(i)], end= " ")