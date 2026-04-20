def solution(record):
    ID_2_Nick = {}
    log = []
    for row in record:
        user = list(row.strip().split())
        
        if user[0] == "Change":
            ID_2_Nick[user[1]] = user[2]
        elif user[0] == 'Enter':
            ID_2_Nick[user[1]] = user[2]
            log.append((user[0], user[1]))
        else:
            log.append((user[0], user[1]))
    
    answer = []
    for row in log:
        if row[0] == 'Enter':
            answer.append(f'{ID_2_Nick[row[1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{ID_2_Nick[row[1]]}님이 나갔습니다.')
    
    return answer