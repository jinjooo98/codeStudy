from collections import deque
import sys

while True:
    rc = list(map(int, sys.stdin.readline().split()))
    n = rc.pop(0)

    if n == 0:
        break

    stack = deque()
    answer = 0
    for i in range(n):
        while len(stack) != 0 and rc[stack[-1]] > rc[i]:
            temp = stack.pop()

            if len(stack) == 0:
                w = i
            else:
                w = i - stack[-1] - 1
            answer = max(answer, w*rc[temp])
        stack.append(i)

    while len(stack) != 0:
        temp = stack.pop()
        if len(stack) == 0:
            w = n
        else:
            w = n - stack[-1] - 1
        answer = max(answer, w*rc[temp])

    print(answer)