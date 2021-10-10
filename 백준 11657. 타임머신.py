import sys
input = sys.stdin.readline

def bellmanFord():
    global Flag
    for repeat in range(N):
        for i in range(1, N + 1):
            for x, y in m[i]:
                if d[i] != INF and d[y] > d[i] + x:
                    d[y] = d[i] + x
                    if repeat == N - 1:
                        Flag = False


N, M = map(int, input().split())
m = [[] for _ in range(N + 1)]
INF = 2147483647
d = [INF] * (N + 1)
d[1] = 0
Flag = True

for _ in range(M):
    a, b, c = map(int, input().split())
    m[a].append((c, b))

bellmanFord()
if not Flag:
    print(-1)
else:
    for l in d[2:]:
        print(l if l != INF else -1)