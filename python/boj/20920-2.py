import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
pq = []
word_cnt_map = {

}

for _ in range(N):
    word = input().strip()

    if len(word) < K:
        pass
    else:
        if word in word_cnt_map:
            word_cnt_map[word] += 1
        else:
            word_cnt_map[word] = 1
    
for word in word_cnt_map:
    heapq.heappush(pq, (-1 * word_cnt_map[word], -1 * len(word), word))

while pq:
    cnt, length, word = heapq.heappop(pq)

    print(word)