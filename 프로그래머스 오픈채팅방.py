def solution(record):
    result = []
    users = dict()
    mode = []

    for x in record:
        m = x.split()[0]
        id = x.split()[1]

        if m in ('Enter', 'Change'):
            nick = x.split()[2]
            users[id] = nick
        mode.append((m, id))

    for x in mode:
        m = x[0]
        id = x[1]
        if m == 'Enter':
            result.append(f'{users[id]}님이 들어왔습니다.')
        elif m == 'Leave':
            result.append(f'{users[id]}님이 나갔습니다.')

    return result