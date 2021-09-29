from heapq import heappop, heappush
n = int(input())
fish = [list(map(int, input().split())) for _ in range(n)]
sharkX, sharkY = 0, 0
for i in range(n):
    for j in range(n):
        if fish[i][j] == 9:
            sharkX, sharkY=(i, j)
            fish[i][j] = 0

dx=[1,-1,0,0]
dy=[0,0,1,-1]
size, move, eat = 2, 0, 0

def bfs(x,y, size, move, eat):
    c=[[False]*n for _ in range(n)]
    q=[]
    heappush(q,(0,x,y))
    while q:
        d, x, y = heappop(q)
        if 0 < fish[x][y] < size:
            move += 1
            fish[x][y] = 0
            if move == size:
                size += 1
                move = 0
            eat += d
            d = 0
            q.clear()
            c = [[False]*n for _ in range(n)]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and fish[nx][ny] <= size and not c[nx][ny]:
                c[nx][ny] = True
                heappush(q,(d+1,nx,ny))
    print(eat)
bfs(sharkX, sharkY, size, move, eat)