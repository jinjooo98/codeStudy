from collections import Counter

def solution(str1, str2):
    low1 = str1.lower()
    low2 = str2.lower()
    lst1 = []
    lst2 = []

    for i in range(len(low1) - 1):
        if low1[i].isalpha() and low1[i + 1].isalpha():
            lst1.append(low1[i] + low1[i + 1])

    for j in range(len(low2) - 1):
        if low2[j].isalpha() and low2[j + 1].isalpha():
            lst2.append(low2[j] + low2[j + 1])

    c1 = Counter(lst1)
    c2 = Counter(lst2)
    i = list((c1 & c2).elements())
    u = list((c1 | c2).elements())

    if len(u) == 0 and len(i) == 0:
        return 65536
    else:
        return int(len(i) / len(u) * 65536)