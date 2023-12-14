import sys

def add(x):
    global S
    if x not in S:
        S.add(x)

def remove(x):
    global S
    if x in S:
        S.remove(x)

def check(x):
    global S
    if x not in S: print(0)
    else: print(1)

def toggle(x):
    global S
    if x not in S: add(x)
    else: remove(x)

def all():
    global S
    S = set(i for i in range(1, 21))

def empty():
    global S
    S.clear()

S = set()
func = {"add": add, "remove": remove, "check": check, "toggle": toggle,\
        "all": all, "empty": empty}

M = int(sys.stdin.readline().strip())
for _ in range(M):
    command = list(sys.stdin.readline().strip().split())
    
    if len(command) > 1:
        func[command[0]](int(command[1]))
    else:
        func[command[0]]()