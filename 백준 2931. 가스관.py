from collections import deque
import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def direction(s):
    if s == '|':
        return [1, 3]
    elif s == '-':
        return [0, 2]
    elif s == '+' or s == 'M' or s == 'Z':
        return [0, 1, 2, 3]
    elif s == '1':
        return [0, 1]
    elif s == '2':
        return [0, 3]
    elif s == '3':
        return [2, 3]
    elif s == '4':
        return [1, 2]

def bfs(x, y, dir):
    global cx, cy
    q = deque()
    q.append([x, y, dir])
    c[x][y] = 1
    while q:
        x, y, dir = q.popleft()
        for i in dir:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not c[nx][ny]:
                if a[nx][ny] != '.':
                    c[nx][ny] = 1
                    ndir = direction(a[nx][ny])
                    q.append([nx, ny, ndir])
                else:
                    if a[x][y] == 'M' or a[x][y] == 'Z':
                        continue
                    if not cx and not cy:
                        cx, cy = nx + 1, ny + 1
                    ix = (i+2) % 4
                    if ix not in check:
                        check.append(ix)

R, C = map(int, input().split())
c = [[0] * C for _ in range(R)]

a = []
for i in range(R):
    row = list(input().strip())
    a.append(row)
    for j in range(C):
        if row[j] == 'M':
            sx, sy = i, j
        elif row[j] == 'Z':
            zx, zy = i, j

check, cx, cy = [], 0, 0
bfs(sx, sy, [0, 1, 2, 3])
bfs(zx, zy, [0, 1, 2, 3])

for i in range(R):
    for j in range(C):
        if a[i][j] != '.' and not c[i][j]:
            bfs(i, j, direction(a[i][j]))
check.sort()

if len(check) == 4:
    print(cx, cy, '+')
else:
    block = ['|', '-', '1', '2', '3', '4']
    for s in block:
        if check == direction(s):
            print(cx, cy, s)