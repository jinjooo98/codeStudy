def mul(n,m1,m2):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= 1000
    return result

def two_div(n,b,m):
    if b == 1 :
        return m
    elif b == 2 :
        return mul(n,m,m)
    else:
        tmp = two_div(n,b//2,m)
        if b%2 == 0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp), m)

n, b = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(n)]
result = two_div(n,b,x)
for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()
