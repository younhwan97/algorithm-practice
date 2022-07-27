import sys, copy
sys.setrecursionlimit(10 ** 6)

def search(x, y, N, M):
    graph[x][y] = -1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                graph_copy[nx][ny] += 1
            elif graph[nx][ny] == 0:
                search(nx, ny, N, M)

## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N): graph.append(list(map(int, sys.stdin.readline().split())))

graph_copy = []
for i in range(0, len(graph)):graph_copy.append(graph[i].copy())

## 결과
time = 0

## 탐색
finish_loof = False
while True:
    if finish_loof:
        print(time)
        break
    else:
        time += 1

        ## 탐색 시작 -> 결과로 1시간 뒤 그래프 생성
        search(0, 0, N, M)

        for i in range(N):
            for j in range(M):
                if graph_copy[i][j] >= 3:
                    graph_copy[i][j] = 0
                elif graph_copy[i][j] == 2 or graph_copy[i][j] == 1:
                    graph_copy[i][j] = 1

        ## 그래프-카피에 담겨져 있는 1시간 뒤 그래프를 본래 그래프 리스트에 복사
        graph = []
        for i in range(0, len(graph_copy)): graph.append(graph_copy[i].copy())

        ## 종료 조건 체크
        finish_loof = True
        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0:
                    finish_loof = False