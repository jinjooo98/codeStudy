from collections import deque

w, h = map(int, input().split())
a = [input() for _ in range(h)]
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            while True:
                if not(0<=nx<h and 0<=ny<w): break
                if a[nx][ny] == '*': break
                if visited[nx][ny] < visited[x][y]+1: break
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx += dx[i]
                ny += dy[i]

C = []
for i in range(h):
    for j in range(w):
        if a[i][j] == 'C':
            C.append((i,j))
(x1, y1), (x2, y2) = C
visited = [[float('inf')]*w for _ in range(h)]
bfs(x1, y1)

print(visited[y1][y2]-1)  #이동한 횟수 - 1 = 거울의 개수