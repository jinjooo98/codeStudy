N = int(input())
s = [list(map(int, input().split())) for i in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(1, N):
    for j in range(N - i):
        x = j + i
        if i == 1:
            dp[j][x] = s[j][0] * s[j][1] * s[x][1]
            continue

        dp[j][x] = 2 ** 32
        for k in range(j, x):
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + s[j][0] * s[k][1] * s[x][1])
print(dp[0][N - 1])
