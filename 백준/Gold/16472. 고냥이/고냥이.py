import sys

n = int(sys.stdin.readline().strip())
language = list(sys.stdin.readline().strip())

ans, cnt = 0, 1
left = 0
word = {language[left]: 1}
for right in range(1, len(language)):
    if language[right] not in word:
        word[language[right]] = 1
        cnt += 1
    else:
        if not word[language[right]]:
            cnt += 1
        
        word[language[right]] += 1
    
    while cnt > n:
        word[language[left]] -= 1
        if not word[language[left]]:
            cnt -= 1
        
        left += 1
    ans = max(ans, right - left + 1)

print(ans)