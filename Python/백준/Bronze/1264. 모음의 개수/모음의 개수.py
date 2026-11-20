import sys
input = sys.stdin.readline

keys = ['a', 'e', 'i', 'o', 'u']

while 1:
	q = input().strip()
	cnt = 0
	if len(q) == 1 and q[0] == '#':
		break
	else:
		for i in q:
			if not i.isalpha():
				continue
			if i.lower() in keys:
				cnt += 1
		print(cnt)
