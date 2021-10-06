n, k = input().split()
k = int(k)
N = len(n)
S = {n}
for _ in range(k):
    if len(S) == 0:
        break;
    new = set()
    while S:
        nums = list(S.pop())
        for i in range(N-1):
            for j in range(i+1,N):
                n = nums[:]
                n[i], n[j] = n[j], n[i]
                if n[0] != '0':
                    new.add(''.join(n))
    S = new
if len(S) == 0:
    print(-1)
else:
    print(max(S))