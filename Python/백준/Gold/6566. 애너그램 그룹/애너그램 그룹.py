import sys

Dict = {}
for _ in range(30000):
    word = sys.stdin.readline().strip()
    if not word: break

    key = "".join(sorted(list(word)))
    if key not in Dict: Dict[key] = [word]
    else: Dict[key].append(word)

values = sorted(Dict.values(), key= lambda x: (-len(x), x))
for ans in values[: 5]:
    print(f'Group of size {len(ans)}:', end=" ")
    print(*sorted(list(set(ans))), sep=" ", end=" .\n")