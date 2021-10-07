p, q, r = [[i for i in map(int, input().split())] for _ in range(3)]
k = (q[0]-p[0]) * (r[1]-p[1]) - (q[1]-p[1]) * (r[0]-p[0])

if k > 0:
    print(1)
elif k < 0:
    print(-1)
else:
    print(0)
