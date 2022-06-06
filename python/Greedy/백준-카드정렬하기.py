import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
que = PriorityQueue()
answer = 0

for _ in range(N):
    que.put(int(sys.stdin.readline()))

while True:
    if que.qsize() == 1:
        break
    else:
        temp = que.get() + que.get()
        answer += temp
        que.put(temp)

print(answer)

## 리스트로 풀이했을 때 "시간초과" 발생