# 2 <= N <= 100,000
# 2 <= L <= 1,000,000
class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr = self.head
        curr.count += 1
        
        for char in string:
            if char not in curr.children:
                curr.children[char] = Node(char)
            
            curr = curr.children[char]
            curr.count += 1
        
        curr.data = string
    
    def search(self, string):
        curr = self.head
        
        cnt = 0
        for char in string:
            cnt += 1
            curr = curr.children[char]
            if curr.count == 1:
                break
        
        return cnt
                
def solution(words):
    N = len(words)
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    answer = 0
    for word in words:
        cnt = trie.search(word)
        print(cnt)
        answer += cnt
        
    return answer

"""
N개의 단어가 주어질 때

"""