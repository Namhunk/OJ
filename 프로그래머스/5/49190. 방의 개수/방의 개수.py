# 1 <= len(arrows) <= 100,000
# 1 <= arrows[i] <= 7

move = {
        0: (-1, 0), 1: (-1, 1),
        2: (0, 1),  3: (1, 1),
        4: (1, 0),  5: (1, -1),
        6: (0, -1), 7: (-1, -1)
    }

def solution(arrows):

    node = set()
    edge = set()
    
    e, n = 0, 0
    x, y = 0, 0
    node.add((x, y))
    for i in arrows:
        r, c = move[i]
        nx, ny = x+r, y+c
        ni = (i+4) % 8
        
        if (x, y, i) not in edge and (nx, ny, ni) not in edge:
            if i % 2 == 1:
                i1 = (i-1)
                i2 = (i+1)%8
                i3 = (i1+3)%8
                i4 = (i2+5)%8
                
                r1, c1 = move[i1]
                r2, c2 = move[i2]
                if (x+r1, y+c1, i3) in edge or (x+r2, y+c2, i4) in edge:
                    e += 2
                    n += 1
                
            node.add((nx, ny))
            edge.add((x, y, i))
        
        x += r
        y += c
    
    e += len(edge)
    n += len(node)
    return 1 - n + e


"""
방을 만드려면 새로운 위치에 새로운 방향으로 나아 가야 함

사각형 안에 대각선 2개가 교차한다면 4개의 방이 만들어짐
1 + 5 
"""