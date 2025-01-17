import sys
input = sys.stdin.readline

# A가 1인 모든 입력에 대해서, 꺼낼 사탕의 맛의 번호를 출력

# 각 사탕의 맛은 좋고 나쁨이 1 - 1,000,000까지의 정수로 구분 1은 가장 맛있는 사탕
# 처음은 빈 사탕상자에서 시작, 사탕의 총 개수는 2,000,000,000을 넘지 않음
# 없는 사탕을 꺼내는 경우와 같은 잘못된 입력은 주어지지 않음

# 수정이가 사탕상자에 손을 댄 횟수 n(1 <= n <= 100,000)
n = int(input().strip())

MAX = 10**6
tree = [0] * (4*MAX+1) # 각 1,000,000 가지 맛에 대한 사탕들의 합

def update(l, r, idx, b, c): # 보유중인 사탕의 개수 변경
    # l, r = 범위, idx = 총 개수, b = 맛, c = 추가할 개수
    tree[idx] += c
    if l == r:
        return

    m = (l + r) // 2
    if b <= m:
        update(l, m, idx*2, b, c)
    else:
        update(m+1, r, idx*2+1, b, c)

def find(l, r, idx, b): # 각 맛에 대해 순위가 b인 사탕을 꺼냄
    tree[idx] -= 1
    if l == r:
        return l

    m = (l + r) // 2
    if tree[idx*2] >= b: # 각 맛의 합의 사탕이 b보다 크면 꺼냄
        return find(l, m, idx*2, b)
    else:
        return find(m+1, r, idx*2+1, b-tree[idx*2])


# 다음 n개의 줄에는 두 정수 A, B 혹은 세 정수 A, B, C 가 주어짐
for _ in range(n):
    # A = 1 : 사탕을 꺼냄, B : 꺼낼 사탕의 순위
    # A = 2 : 사탕을 넣음, B : 넣을 사탕의 맛, C = 양수 : 몇개 넣는지, C = 음수 : 몇개 빼는지
    canddy = list(map(int, input().strip().split()))
    if canddy[0] == 1:
        print(find(1, MAX, 1, canddy[1]))

    else:
        update(1, MAX, 1, canddy[1], canddy[2])
