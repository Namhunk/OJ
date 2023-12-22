import sys

# 문자열 안에 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며 남은 문자열은 합쳐짐
# -폭발 과정-
# 1. 문자열이 폭발 문자열을 포함하고 있는 경우, 모든 폭발 문자열이 폭발하게 됨.
# 남은 문자열을 이어 붙여 새로운 문자열을 만듬
# 2. 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있음
# 3. 폭발은 폭발 문자열이 문자열에 없을 때까지 계속됨

# 모든 폭발이 끝난 후 어떤 문자열이 남았는지 출력, 문자가 없는 경우 "FRULA" 출력

# 문자열 입력
string = list(sys.stdin.readline().strip())

# 폭발 문자열 입력
bomb = list(sys.stdin.readline().strip())

# 스택에 문자열의 문자들을 순서대로 저장하며 스택의 끝에서 폭발 문자열의 길이만큼이
# 폭발 문자열과 같다면 폭발 문자열의 길이만큼 pop 진행

stack = [] # 스택 생성
for i in string:
    stack.append(i)
    while len(stack) >= len(bomb) and stack[len(stack)-len(bomb): len(stack)] == bomb:
        for _ in range(len(bomb)):
            stack.pop()
    
print(''.join(stack) if stack else "FRULA") # 문자가 존재하면 출력 아니면 FRULA 출력