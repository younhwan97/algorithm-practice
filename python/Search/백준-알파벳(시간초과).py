import sys, copy
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
R, C = map(int, sys.stdin.readline().split())

graph = []
for _ in range(R): graph.append(list(sys.stdin.readline().strip()))

def search(x, y, s):
    print(1)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
       
        if (0 <= nx < R) and (0 <= ny < C):
            if graph[nx][ny] not in alph:
                if s + 1 > step[nx][ny]:
                    step[nx][ny] = s + 1

                alph.add(graph[nx][ny])
                search(nx, ny, s + 1)
                alph.remove(graph[nx][ny])

## 결과
step = [[0] * C for _ in range(R)]

## 탐색
alph = set()
alph.add(graph[0][0])
search(0, 0, 1)

## 결과 출력
print(max(map(max, step)))