def solution(numbers, target):
    root = [0]
    for i in numbers:
        tmp = []
        for j in root:
            tmp.append(j + i)
            tmp.append(j - i)
        root = tmp

    answer = root.count(target)
    return answer