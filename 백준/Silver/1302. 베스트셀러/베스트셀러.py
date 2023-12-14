import sys

n = int(sys.stdin.readline().strip())
Dict = {}
for _ in range(n):
    title = sys.stdin.readline().strip()

    if title not in Dict: Dict[title] = 1
    else: Dict[title] += 1

MAX = max(Dict.values())
books = []
for i in Dict.keys():
    if Dict[i] == MAX: books.append(i)

print(sorted(books)[0])