from collections import deque
import sys

maps = []
swans = []
r, c = map(int, sys.stdin.readline().split())

for y in range(r):
    arr = list(sys.stdin.readline().replace("\n", ""))
    maps.append(arr)
    for x in range(len(arr)):
        if arr[x] == "L":
            swans.append((y, x))
t = [[0 for _ in range(c)] for _ in range(r)]

def melt(maps: list) -> int:
    visited = [[False for _ in range(c)] for _ in range(r)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]

    queue = deque()
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == '.' or maps[y][x] == 'L':
                queue.append((y, x))
                t[y][x] = 0
                visited[y][x] = True

    l_time = 0
    while queue:
        y, x = queue.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != 'L':
                queue.append((ny, nx))
                t[ny][nx] = t[y][x] + 1
                visited[ny][nx] = True
                l_time = t[ny][nx]
    return l_time

def bfs(start: tuple, maps: list, mid: int, end: tuple) -> bool:
    dirs =[(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque()
    queue.append(start)
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx]:
                visited[ny][nx] = True
                if ny == end[0] and nx == end[1]:
                    return True
                if t[ny][nx] <= mid:
                    queue.append((ny, nx))
    return False

_min, _max = 0, melt(maps)
answer = _max
while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(swans[0], maps, mid, swans[1]):
        answer = mid
        _max = mid - 1
    else:
        _min = mid + 1
print(answer)


