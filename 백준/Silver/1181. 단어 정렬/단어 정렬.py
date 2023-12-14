import sys
dic = {key : [] for key in range(1, 51)}
for num in range(int(sys.stdin.readline().strip())):
    word = sys.stdin.readline().strip()
    if word not in dic[len(word)]:
        dic[len(word)].append(word)
        dic[len(word)].sort()

for wordlist in dic.values():
    if wordlist != None:
        for word in wordlist:
            print(word)