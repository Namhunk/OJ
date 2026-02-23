import sys
input = sys.stdin.readline

class Properties:
    def __init__(self, POSITION=(0, 0), SIZE=(0, 0), COLOR=1, PARENT_ORIGIN=(0, 0),
                 ANCHOR_POINT=(0, 0), SENSITIVE=1, CLIP_CHILD=0, SCREEN_POSITION=(0, 0)):
        self.POSITION        = POSITION
        self.SIZE            = SIZE
        self.COLOR           = COLOR
        self.PARENT_ORIGIN   = PARENT_ORIGIN
        self.ANCHOR_POINT    = ANCHOR_POINT
        self.SENSITIVE       = SENSITIVE
        self.CLIP_CHILD      = CLIP_CHILD
        self.SCREEN_POSITION = SCREEN_POSITION

class Actor:
    def __init__(self, Name: str, is_Window: bool=False):
        self.Name   = Name
        self.Parent = None
        self.Child  = []
        self.Scene_On = 0
        if is_Window:
            self.Property = Properties(POSITION=(0, 0), PARENT_ORIGIN=(0, 0), ANCHOR_POINT=(0, 0),
                                       SIZE=(W, H), COLOR=0, SENSITIVE=1, CLIP_CHILD=1)
            self.Scene_On = 1

        else:
            self.Property = Properties()
            self.Scene_On = 0

# New
def New(actor_name: str):
    var[actor_name] = Actor(actor_name)

# Add
def Add(parent_name, child_name):
    parent = var[parent_name]
    child = var[child_name]
    if child.Parent is not None:
        Unparent(child_name)
    parent.Child.append(child)
    child.Parent = parent

    flag = 1 if parent.Scene_On == 1 else 0
    Scene_off(child, flag)   # child 포함 서브트리 전체 1회 전파

# Remove
def Remove(actor_name: str, actor2_name: str):
    actor  = var[actor_name]
    actor2 = var[actor2_name]

    if actor2 in actor.Child:
        actor.Child.remove(actor2)
        actor2.Parent = None
        Scene_off(actor2, 0)
        Update_Screen_Position(actor2)

# Unparent
def Unparent(actor_name: str):
    actor  = var[actor_name]
    parent = actor.Parent

    if parent != None: # 부모 Actor가 있는 경우
        parent.Child.remove(actor)
        actor.Parent = None
        Scene_off(actor, 0)
        Update_Screen_Position(actor)

# SetProperty
def SetProperty(actor_name: str, prop_name: str, value: list):
    if len(value) > 1:
        value = tuple(map(int, value))
    else:
        value = int(value[0])
    
    actor = var[actor_name]
    setattr(actor.Property, prop_name, value)

# GetProperty
def GetProperty(actor_name: str, prop_name: str):
    actor = var[actor_name]
    val = getattr(actor.Property, prop_name)
    if isinstance(val, tuple):
        print(*val)
    else:
        print(val)

# Touch
def Touch(X: int, Y: int):
    # Touch는 Scene_on=1, SENSITIVE=1 이어야 가능, 부모의 CLIP_CHILD=0 이어야 다음 Actor 가능
    Window = var['Window']
    name = find_Touch(Window, X + 0.5, Y + 0.5)
    if name is None:
        print("Window")
    else:
        print(name)

def find_Touch(root: Actor, X: float, Y: float):
    stack = [(root, False)]
    while stack:
        actor, done = stack.pop()
        if not done:
            # CLIP_CHILD 체크
            if actor.Parent:
                par = actor.Parent
                if par.Property.CLIP_CHILD == 1 and not covers_pixel(par, X, Y):
                    continue
            stack.append((actor, True))         # 자기 자신은 나중에 처리
            for child in actor.Child:           # 정순 push → 역순 pop (LIFO)
                stack.append((child, False))
        else:
            if check(actor, X, Y):             # SENSITIVE 포함 자기 자신 체크
                return actor.Name
    return None

# 현재 Actor의 범위에 X, Y가 있는지, SENSITIVE가 1인지
def check(actor: Actor, X: float, Y: float):
    prop = actor.Property

    ax = prop.SCREEN_POSITION[0]
    ay = prop.SCREEN_POSITION[1]
    w, h = prop.SIZE

    if prop.ANCHOR_POINT[0] == 1:
        ax -= w
    if prop.ANCHOR_POINT[1] == 1:
        ay -= h

    # 한 칸은 [ax, ax+w), [ay, ay+h) 로 보는 게 안전
    return (
        prop.SENSITIVE == 1 and
        w > 0 and h > 0 and
        ax <= X < ax + w and
        ay <= Y < ay + h
    )

# 각 SCREEN_POSITION 업데이트
def Update_Screen_Position(actor: Actor):
    # BFS로 위에서 아래로 순서가 중요하므로 queue 사용
    from collections import deque
    q = deque([actor])
    while q:
        cur = q.popleft()
        prop = cur.Property
        if cur.Name == 'Window' or cur.Scene_On == 0:
            prop.SCREEN_POSITION = (0, 0)
        else:
            pp = cur.Parent.Property
            parent_left = pp.SCREEN_POSITION[0] - pp.ANCHOR_POINT[0] * pp.SIZE[0]
            parent_top  = pp.SCREEN_POSITION[1] - pp.ANCHOR_POINT[1] * pp.SIZE[1]
            ox = parent_left + prop.PARENT_ORIGIN[0] * pp.SIZE[0]
            oy = parent_top  + prop.PARENT_ORIGIN[1] * pp.SIZE[1]
            prop.SCREEN_POSITION = (ox + prop.POSITION[0], oy + prop.POSITION[1])
        q.extend(cur.Child)

def Scene_off(actor, flag):
    stack = [actor]
    while stack:
        cur = stack.pop()
        cur.Scene_On = flag
        stack.extend(cur.Child)

def covers_pixel(actor: Actor, X: float, Y: float) -> bool:
    prop = actor.Property

    ax = prop.SCREEN_POSITION[0]
    ay = prop.SCREEN_POSITION[1]
    w, h = prop.SIZE

    if prop.ANCHOR_POINT[0] == 1:
        ax -= w
    if prop.ANCHOR_POINT[1] == 1:
        ay -= h

    return (
        actor.Scene_On == 1 and
        w > 0 and h > 0 and
        ax <= X < ax + w and
        ay <= Y < ay + h
    )

def find_actor_for_pixel(root, X, Y):
    stack = [(root, False)]
    while stack:
        actor, done = stack.pop()
        if not done:
            if actor.Parent:
                par = actor.Parent
                if par.Property.CLIP_CHILD == 1 and not covers_pixel(par, X, Y):
                    continue
            stack.append((actor, True))
            for child in actor.Child:
                stack.append((child, False))
        else:
            if covers_pixel(actor, X, Y):      # SENSITIVE 미포함
                return actor
    return None

def solve():
    global W, H, var

    # Window 크기 입력 (3 <= W, H <= 50)
    W, H = map(int, input().strip().split())

    # 각 Actor를 이름에 따라 매칭할 변수 생성
    var = {'Window': Actor('Window', is_Window=True)} # Window 기본값 설정

    # 명령어의 개수 Q (3 <= Q <= 5,000)
    Q = int(input().strip())

    for _ in range(Q):
        command = list(input().strip().split())

        # 각 command[0]에 따른 실행
        if command[0] == "New":
            actor_name = command[1]
            New(actor_name)
        
        elif command[0] == 'Add':
            actor_name, actor2_name = command[1], command[2]
            Add(actor_name, actor2_name)

        elif command[0] == 'Remove':
            actor_name, actor2_name = command[1], command[2]
            Remove(actor_name, actor2_name)

        elif command[0] == 'Unparent':
            actor_name = command[1]
            Unparent(actor_name)

        elif command[0] == 'SetProperty':
            actor_name, prop_name = command[1], command[2]
            value = command[3:]
            SetProperty(actor_name, prop_name, value)

        elif command[0] == 'GetProperty':
            actor_name, prop_name = command[1], command[2]
            GetProperty(actor_name, prop_name)

        elif command[0] == 'Touch':
            X, Y = map(int, command[1:])
            Touch(X, Y)
        
        Update_Screen_Position(var['Window'])
    
    # Q개의 명령어가 모두 종료된 뒤 현재 Window에 칠해진 색상을 H줄에 걸쳐 출력
    for i in range(H):
        row = []
        for j in range(W):
            x = j + 0.5
            y = i + 0.5
            actor = find_actor_for_pixel(var['Window'], x, y)
            if actor is None:
                row.append('0')
            else:
                row.append(str(actor.Property.COLOR))
        print(''.join(row))
    
if __name__ == '__main__':
    solve()
