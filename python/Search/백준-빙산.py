import sys
from collections import deque

input = sys.stdin.readline

## 입력 및 그래프 생성
N, M = map(int, input().split())

graph = []
for _ in range(N): graph.append(list(map(int, input().split())))

## 탐색 메서드 정의
def search(x, y):
    

## 탐색
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            
