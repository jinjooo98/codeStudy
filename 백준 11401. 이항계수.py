import sys

N, K = map(int, sys.stdin.readline().split())
m = 1000000007

f=[1]
for i in range(1,N+1):
    f += [f[-1]*i%m]

print(f[N] * pow(f[K] * f[N-K], m-2, m) % m)