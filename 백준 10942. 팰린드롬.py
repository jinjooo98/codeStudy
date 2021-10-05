import sys

input = sys.stdin.readline
n = int(input())
arr = [-1] + list(map(int, input().split()))
m = int(input())

dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n - 1, 0, -1):
    for j in range(n, 1, -1):
        if j > i:
            dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else 0

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])
