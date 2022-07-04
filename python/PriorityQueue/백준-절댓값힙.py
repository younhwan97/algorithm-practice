import sys
from queue import PriorityQueue

N = int(input())

pq = PriorityQueue()

for _ in range(N):
    value = int(sys.stdin.readline())
    abs_value = abs(value)

    if value == 0:
        if pq.qsize() == 0:
            print(0)
        else:
            print((pq.get())[1])
    else:
        pq.put([abs_value, value])

## 알 수 있는 것
## 2차원 리스트를 큐에 삽입할 때 첫번째 원소를 기준으로 처리