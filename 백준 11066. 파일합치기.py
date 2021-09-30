def dp():
    N = int(input())
    P = [0] + list(map(int, input().split()))
    sum = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        sum[i] = sum[i - 1] + P[i]

    DP = [[0 for i in range(N + 1)] for _ in range(N + 1)]

    for i in range(2, N + 1):
        for j in range(1, N + 2 - i):
            DP[j][j + i - 1] = min([DP[j][j + k] + DP[j + k + 1][j + i - 1] for k in range(i - 1)]) \
                               + (sum[j + i - 1] - sum[j - 1])
    print(DP[1][N])


for _ in range(int(input())):
    dp()
