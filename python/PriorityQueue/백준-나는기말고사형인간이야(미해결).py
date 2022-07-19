import sys, heapq

N, M = map(int, sys.stdin.readline().split())
N *= 24

base_score = list(map(int, sys.stdin.readline().split()))
eff = list(map(int, sys.stdin.readline().split()))
pq = []

complete_subject = []

## 공부 효율이 높은 순서대로 우선순위 큐에 담는다.
for i in range(M):
    heapq.heappush(pq, (- 1 * eff[i], -1 * base_score[i]))

while N > 0 and pq:
    temp = heapq.heappop(pq)
    eff = -1 * temp[0]
    score = -1 * temp[1]

    need = (100 - score) // eff ## 60점 3효율 일 때, 40 // 3 -> 13

    if N >= need:
        ## 시간이 충분할 때
        score = score + eff * need
        N -= need
        if score == 100:
            complete_subject.append(100)
        else:
            eff = 100 - score
            heapq.heappush(pq, (-1 * eff, -1 * score))
    else:
        score = score + eff * N
        eff = 100 - score
        heapq.heappush(pq, (-1 * eff, -1 * score))
        N = 0

while pq:
    temp = heapq.heappop(pq)
    score = -1 * temp[1]
    complete_subject.append(score)

print(sum(complete_subject))