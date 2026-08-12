class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}
        self.cnt = 0
class Trie:
    def __init__(self):
        self.front = Node(None)
        self.back = Node(None)
    
    def insert_front(self, word):
        node = self.front
        node.cnt += 1
        for w in word:
            if w not in node.child:
                node.child[w] = Node(w)
            
            node = node.child[w]
            node.cnt += 1
    
    def insert_back(self, word):
        node = self.back
        node.cnt += 1
        for w in reversed(word):
            if w not in node.child:
                node.child[w] = Node(w)
            
            node = node.child[w]
            node.cnt += 1
    
    def search_front(self, word):
        node = self.front
        for w in word:
            # 1. w가 ? 인 경우
            if w == '?':
                return node.cnt
            
            # 2. w가 ?가 아니고 자식들 중에도 없는 경우
            if w not in node.child:
                return 0
            
            node = node.child[w]
    
    def search_back(self, word):
        node = self.back
        for w in reversed(word):
            if w == '?':
                return node.cnt
            
            if w not in node.child:
                return 0
            
            node = node.child[w]
            
def solution(words, queries):
    answer = []
    size = {i: Trie() for i in range(1, 100_000)} # 각 길이에 따른 Trie 분류
    for word in words:
        l = len(word)
        
        size[l].insert_front(word)
        size[l].insert_back(word)
    
    for q in queries:
        l = len(q)
        if l not in size:
            answer.append(0)
            continue
        t = size[l]
        if q[0] != '?':
            answer.append(t.search_front(q))
        else:
            answer.append(t.search_back(q))
        
    return answer
'''
words와 queries가 주어질 때
각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환
?는 키워드의 접두사 또는 접미사 중 하나로만 주어짐
------------------------------------------------------------
2 <= len(words)  <= 100,000
2 <= len(queries) <= 100,000
-------------------------------------
1. 각 words들을 길이별로 분류
2. 현재 queries[i]와 같은 길이의 분류로 이동
3. queries[i]의 접두사, 접미사 확인
4. ?가 아닌 (접두사, 접미사) 위치를 시작 위치로 설정
5. 만약 다음 단어가 ? 라면 현재 누적 개수 return
'''