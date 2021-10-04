import sys
N, M = map(int, sys.stdin.readline().split())

memory = [0] + list(map(int, sys.stdin.readline().split()))
cost = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(sum(cost) + 1 )] for __ in range(len(cost) + 1)]

answer = sum(cost)
for i in range(1, len(cost)):
    for j in range(len(dp[1])):
        if cost[i] > j :
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-cost[i]] + memory[i], dp[i-1][j])

        if dp[i][j] >= M:
            answer = min(answer, j)

print(answer)