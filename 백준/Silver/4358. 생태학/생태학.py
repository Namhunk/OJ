import sys

cnt = 0
Dict = {}
for _ in range(int(1e6)):
    tree = sys.stdin.readline().strip()
    if not tree: break
    cnt += 1
    Dict[tree] = Dict.get(tree, 0) + 1

for i, j in sorted(Dict.items()):
    print(f'{i} {j/cnt*100:.4f}')