import sys
# 다른 방법
INF = int(1e9)
postorder = [] # 배열에는 현재 값과 root 값을 저장(현재, root)

while True:
    try: # 입력이 들어오는 동안
        key = int(sys.stdin.readline().strip())
        # 배열이 비어있지 않고, 현재 값이 root 값보다 크다면 출력
        while postorder and key > postorder[-1][1]: print(postorder.pop()[0])
        # 배열이 비어있으면 추가
        if not postorder: postorder.append((key, INF))
        # 현재 값이 이전 값보다 작으면 -> 이전값이 root
        elif key < postorder[-1][0]: postorder.append((key, postorder[-1][0]))
        # 현재 값이 이전 값보다 크면 -> 이전 값의 root를 가짐
        else: postorder.append((key, postorder[-1][1]))
    except: # 입력이 없다면
        print(*[i[0] for i in postorder[::-1]], sep='\n') # 남은 값들(오른쪽) 부분들을 역순으로 출력
        break