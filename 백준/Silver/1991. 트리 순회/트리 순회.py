import sys

def preorder(start):
    string = ""
    string += start

    left, right = graph[start]
    if left != '.':
        string += preorder(left)
    
    if right != '.':
        string += preorder(right)
    
    return string

def inorder(start):
    string = ""
    left, right = graph[start]

    if left != '.':
        string += inorder(left)
    
    string += start

    if right != '.':
        string += inorder(right)
    
    return string

def postorder(start):
    string = ""

    left, right = graph[start]

    if left != '.':
        string += postorder(left)
    
    if right != '.':
        string += postorder(right)
    
    string += start

    return string

n = int(sys.stdin.readline().strip())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
graph = {i: [] for i in alpha[:n]}

for _ in range(n):
    p, l, r = sys.stdin.readline().strip().split()
    graph[p].append(l)
    graph[p].append(r)

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))