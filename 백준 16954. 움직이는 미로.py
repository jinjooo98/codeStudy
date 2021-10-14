from collections import deque
import sys

input = sys.stdin.readline
maze=[list(input().rstrip()) for _ in range(8)]
d = ((0,1), (0,0), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1))

def bfs(sx, sy, stime):
    q = deque()
    q.append((sx, sy, stime))
    while q:
        x, y, t = q.popleft()
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and not maze[nx-t][ny] == '#' and not maze[nx-t-1][ny] == '#':
                if nx-t < 0:
                    return 1
                q.append([nx, ny, t+1])
    return 0

print(bfs(7,0,0))