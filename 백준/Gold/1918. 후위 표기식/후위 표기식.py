import sys

string = sys.stdin.readline().strip()
stack = []
ans = ""

# 각 연산에 우선순위 부여
prior = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
for i in string:
    # 문자인 경우 문자열에 추가
    if i.isalpha(): ans += i
    elif i == '(': stack.append(i)
    elif i == ')':
        while stack[-1] != '(':
            ans += stack.pop()
        
        stack.pop()
    
    else:
        while stack and prior[i] <= prior[stack[-1]]:
            ans += stack.pop()
        
        stack.append(i)

# 스택에 남은 연산기호 추가
while stack:
    ans += stack.pop()

print(ans)