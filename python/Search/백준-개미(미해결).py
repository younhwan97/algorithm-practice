import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

## 입력
n = int(input())

energy = []
for _ in range(n): energy.append(int(input()))

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    start, end, weight = map(int, input().split())
    graph[end].append((start, weight))

arrivals = [-1] * (n + 1)
arrivals[1] = 1

## 탐색 메서드 정의
def search(num, energy):
    global start
    global arrive

    visited[num] = True

    if energy >= 0:
        arrive = num

    if num == 1:
        arrivals[start] = arrive
        return

    for i in graph[num]:
        v, e = i
        if not visited[v]:
            search(v, energy - e)
    
    if arrivals[start] == -1:
        arrivals[start] = start

## 탐색
for i in range(2, n + 1):
    start = i
    arrive = 0

    visited = [False] * (n + 1)
    search(i, energy[i - 1])

for i in range(1, n + 1):
    print(arrivals[i])