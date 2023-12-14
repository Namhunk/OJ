S = input().upper()
dict = {}
for i in S:
    if i not in dict: dict[i] = S.count(i)
key = ""; value = 0
for i in dict:
    if dict[i] > value:
        key = i
        value = dict[i]
    elif dict[i] == value:
        key = ""
if key == "":
    print("?")
else: print(key)