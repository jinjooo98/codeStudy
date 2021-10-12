import sys
T = int(input())
INF = float('inf')
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    ticket = [[] for _ in range(N + 1)]

    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        ticket[u].append([v, c, d])
        dp = [[INF for _ in range(M + 1)] for _ in range(N + 1)]
        dp[1][0] = 0

        for c in range(M + 1):
            for d in range(1, N + 1):
                if dp[d][c] == INF:
                    continue
                t = dp[d][c]
                for tv, tc, td in ticket[d]:
                    if tc + c > M:
                        continue
                    dp[tv][tc + c] = min(dp[tv][tc + c], t + td)
    result = min(dp[N])

    if result == INF:
        print('Poor KCM')
    else:
        print(result)
