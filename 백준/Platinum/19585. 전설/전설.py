import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.child = {}
        self.last = False
    
class Trie:
    def __init__(self):
        self.head = Node()
    
    def insert(self, string):
        curr = self.head

        for char in string:
            if char not in curr.child:
                curr.child[char] = Node()
            
            curr = curr.child[char]
        
        curr.last = True
    

def solve():
    # (1 <= C, N <= 4,000)
    C, N = map(int, input().strip().split())

    Color = {input().strip() for _ in range(C)} # 색상, unique

    Name = {input().strip() for _ in range(N)} # 이름, unique

    CT = Trie()
    for color in Color:
        CT.insert(color)

    # Q (1 <= Q <= 20,000)
    Q = int(input().strip())
    
    for _ in range(Q):
        Team = input().strip()
        L = len(Team)

        node = CT.head
        check = False

        for i in range(L):
            ch = Team[i]
            if ch not in node.child: break
            node = node.child[ch]
            if node.last and Team[i+1:] in Name:
                check = True
                break
                
        print('Yes' if check else 'No')

if __name__ == '__main__':
    solve()

"""
색상 이름과 닉네임의 순서로 이여서 팀명을 지으면 수상할 수 있다는 전설이 있음
각 팀들이 우승할 수 있는지

20,000 x 2,000
최대 4 x 10^7 개를 검사

각 길이 L의 문자열이

"""