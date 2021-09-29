import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    answer = 0
    answer_ = []
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i + 1))

    time = 0
    prev = 0
    flag = True
    while flag:
        length = len(hq)
        time += (hq[0][0] - prev) * length
        if time > k:
            time -= (hq[0][0] - prev) * length
            while hq:
                answer_.append(heapq.heappop(hq)[1])
            answer_.sort()
            answer = answer_[(k - time) % length]
            flag = False
        else:
            prev = heapq.heappop(hq)[0]

    return answer