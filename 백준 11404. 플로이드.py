import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
inf = 100000000
g = [[inf] * n for i in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    if g[a - 1][b - 1] > c:
        g[a - 1][b - 1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and g[i][j] > g[i][k] + g[k][j]:
                g[i][j] = g[i][k] + g[k][j]
for i in g:
    for j in i:
        if j == inf:
            print(0, end=' ')
        else:
            print(j, end=' ')
    print()