import sys
# 동1 , 서2, 남3, 북4

K = int(sys.stdin.readline().strip())

vw = []
mw = []
vh = []
mh = []

for _ in range(6):
    v, w = map(int, sys.stdin.readline().strip().split())
    if v == 1 or v == 2: vw.append(v); mw.append(w)
    if v == 3 or v == 4: vh.append(v); mh.append(w)

area = 1
marea = 1
H = 0
W = 0
for i in vw:
    if vw.count(i) == 1:
        W = i
        area*= mw[vw.index(i)]

for i in vh:
    if vh.count(i) == 1:
        H = i
        area*= mh[vh.index(i)]

if W == 1:
    if H == 4:
        marea*= mw[vw.index(W)-1]
        marea*= mh[vh.index(H)-2]
    else:
        marea*= mw[vw.index(W)-2]
        marea*= mh[vh.index(H)-1]
else:
    if H == 4:
        marea*= mw[vw.index(W)-2]
        marea*= mh[vh.index(H)-1]
    else:
        marea*= mw[vw.index(W)-1]
        marea*= mh[vh.index(H)-2]

print(K * (area - marea))
