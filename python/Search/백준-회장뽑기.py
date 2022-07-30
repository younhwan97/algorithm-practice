import sys
from collections import deque

## 입력 및 그래프 생성
n = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1:
        break
    else:
        graph[a].append(b)
        graph[b].append(a)

## 탐색 메서드 정의
def search(start):
    distance[start] = 0

    ## 큐 생성
    que = deque()
    que.append(start)

    ## 반복
    score = 0
    while que:
        v = que.popleft()

        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                que.append(i)
        
        score += 1

## 탐색
result = [0] * (n + 1)
distance = [-1] * (n + 1)

for i in range(1, n + 1):
    search(i)
    result[i] = max(distance)
    distance = [-1] * (n + 1)

## 결과
min_value = result[1]
min_number = []

for i in range(2, len(result)):
    if result[i] < min_value:
        min_value = result[i]

for i in range(0, len(result)):
    if result[i] == min_value:
        min_number.append(i)

print(min_value, len(min_number))
for i in range(0, len(min_number)):
    print(min_number[i], end =" ")