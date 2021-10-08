from collections import deque

n = int(input())
m = [list(map(int, input().split())) for i in range(n)]

mL = set()
for i in range(n):
    for j in range(n):
        mL.add(m[i][j])
mL = list(mL)
mL.sort()

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
a, b = 0, 0
q = deque()

ans = float('inf')

while a < len(mL):
    go = False
    if mL[a] <= m[0][0] <= mL[b]:
        d = [[0] * n for _ in range(n)]
        q.clear()
        q.append((0, 0))
        d[0][0] = 1

        while q:
            x, y, = q.popleft()
            if (x, y) == (n - 1, n - 1):
                go = True
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= n or ny >= n or d[nx][ny] != 0:
                    continue
                if mL[a] <= m[nx][ny] <= mL[b]:
                    d[nx][ny] = 1
                    q.append((nx, ny))

    if go:
        ans = min(ans, mL[b] - mL[a])
        a += 1
    elif b < len(mL) - 1:
        b += 1
    else:
        break
print(ans)