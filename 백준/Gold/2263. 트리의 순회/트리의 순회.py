import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)
# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다.
# 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성
# 첫째 줄에 프리오더를 출력

# n (1 <= n <= 100,000)
n = int(input().strip())

# 인오더를 나타내는 n개의 자연수
Inoder = list(map(int, input().strip().split()))

# 포스트오더를 나타내는 n개의 자연수
Postoder = list(map(int, input().strip().split()))

# Inoder : left -> root -> right
# Postoder : left -> right -> root
# Preoder : root -> left -> right

# Inoder의 root를 기준으로 left, right 를 분할
# Postoder의 마지막 값은 root값이 옴

idx = [0]*(n+1) # Inoder의 값들이 어느 위치에 있는지 저장
for i in range(n):
    idx[Inoder[i]] = i

def Preoder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end): return # 두 범위 사이의 값이 없을때 까지

    parent = Postoder[post_end] # root값은 Postoder의 끝에 위치

    print(parent, end=' ') # 출력

    left = idx[parent] - in_start # root 왼쪽의 길이
    right = in_end - idx[parent] # root 오른쪽의 길이

    Preoder(in_start, in_start+left-1, post_start, post_start+left-1)
    Preoder(in_end-right+1, in_end, post_end-right, post_end-1)

Preoder(0, n-1, 0, n-1)