import sys, heapq

N, M = map(int, sys.stdin.readline().split())

N *= 24

pq = []

base_score = []
study_eff = []

for i in range(2):
    if i == 0:
        base_score = list(map(int, sys.stdin.readline().split()))
    else:
        study_eff = list(map(int, sys.stdin.readline().split()))

for i in range(0, len(base_score)):
    heapq.heappush(pq, (-1 * study_eff[i], base_score[i]))

subject_arr = []

while N > 0 and len(pq) != 0:
    subject = heapq.heappop(pq)

    eff = -1 * subject[0] # 과목을 1시간 공부할 때 얻을 수 있는 효율
    score = subject[1] # 점수

    if 100 > eff + score:
        temp = (100 - score) // eff ## 50, 4 일때는 12이고, 32, 40 일때는 1

        if temp > N:
            ## 투자해야할 시간이 남은 시간을 초과할 때
            temp = N
    
        score = temp * eff + score

        if score > 100:
            score = 100
            subject_arr.append(100)
        else:
            eff = 100 - score
            heapq.heappush(pq, (-1 * eff, score))

        N -= temp
    elif 100 <= eff + score:
        subject_arr.append(100)
        N -= 1

while len(pq) > 0:
    subject = heapq.heappop(pq)
    subject_arr.append(subject[1])

print(sum(subject_arr))