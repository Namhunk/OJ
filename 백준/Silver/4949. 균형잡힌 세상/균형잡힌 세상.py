import sys
string_list = []
while True:
    string = sys.stdin.readline().rstrip()
    if string == ".": break
    string_list.append(string)

for s in string_list:
    stack1 = []
    stack2 = []
    for word in s:
        if word in "([": stack1.append(word)
        elif word in "])":
            if len(stack1) != 0:
                if word == ")":
                    if stack1[-1] == "(": stack1.pop()
                    elif stack1[-1] == "[": break
                elif word == "]":
                    if stack1[-1] == "[": stack1.pop()
                    elif stack1[-1] == "(": break
            else: stack2.append(word)

    if len(stack1) == 0 and len(stack2) == 0: print('yes')
    else: print('no')