import sys
input = sys.stdin.readline

# 각 단어를 입력하기 위해 버튼을 눌러야 하는 횟수의 평균을 소수점 둘째 자리까지 반올림 하여 출력

class Node:
    def __init__(self, key):
        self.key = key
        self.child = []
        self.last = False

def trie(words):
    tri = Node('-')
    curr = tri

    for word in words:
        for alpha in word:
            curr = search(curr, alpha)
        curr.last = True
        curr = tri
    return tri

def get_cnt(curr, cnt):
    global ans
    if curr.last:
        ans += cnt
    if curr.child:
        if not curr.last and len(curr.child) == 1:
            get_cnt(curr.child[0], cnt)
        else:
            for child in curr.child:
                get_cnt(child, cnt+1)

def search(curr, target):
    for child in curr.child:
        if child.key == target:
            return child

    node = Node(target)
    curr.child.append(node)
    return node

while 1: # 여러 개의 테스트 케이스
    # 사전에 속한 단어의 개수 N (1 <= N <= 10**5)
    N = input().strip()
    if N == '': break
    N = int(N)

    # N개의 영단어 각 단어의 길이 총합은 최대 10**6
    words = [input().strip() for _ in range(N)] # 길이별로 정렬
    ans = 0

    tri = trie(words)
    for child in tri.child:
        get_cnt(child, 1)

    print(f'{round(ans/N, 2):.2f}')