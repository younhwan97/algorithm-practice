import sys
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
R, C = map(int, sys.stdin.readline().split())

graph = []
for _ in range(R): graph.append(list(sys.stdin.readline().strip()))

## 탐색 메서드 정의
def search(x, y, length):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 < nx < R) and (0 < ny < C):
            if graph[nx][ny] not in visitied_alph:
                if distance[nx][ny] == -1:
                    distance[nx][ny] = length + 1

                    visitied_alph.append(graph[nx][ny])
                    search(nx, ny, length + 1) 
                    visitied_alph.remove(graph[nx][ny])
                else:
                    if distance[nx][ny] <= length + 1:
                        distance[nx][ny] = length + 1

                        visitied_alph.append(graph[nx][ny])
                        search(nx, ny, length + 1) 
                        visitied_alph.remove(graph[nx][ny])

## 탐색
distance = [[-1] * C for _ in range(R)]
distance[0][0] = 1

visitied_alph = []
visitied_alph.append(graph[0][0])

search(0, 0, 1)

## 결과 출력
print(max(map(max, distance)))