import sys, copy
sys.setrecursionlimit(10 ** 6)

def search(x, y, N, M):
    global cnt 

    ## 현재 지점은 다시 방문하지 않도록 값을 변경한다.
    graph[x][y] = -1

    ## 상, 하, 좌, 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < M):
            if graph[nx][ny] == 1:
                ## 공기와 맞닿는 치즈가 존재할 때
                ## 그래프-카피의 경우 한시간 뒤 그래프의 상태를 그린다.
                if graph_copy[nx][ny] != 0:
                    graph_copy[nx][ny] = 0
                    cnt += 1
            elif graph[nx][ny] == 0:
                search(nx, ny, N, M)
 
## 입력 및 그래프 생성
N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

graph_copy = []
for i in range(0, len(graph)):
    graph_copy.append(graph[i].copy())

## 결과
time = 0
finish_loof = False
cnt = 0

## 탐색
while True:
    if finish_loof:
        break
    else:
        time += 1
        cnt = 0

        search(0, 0, N, M)
        
        graph = []

        for i in range(0, len(graph_copy)):
            graph.append(graph_copy[i].copy())

        finish_loof = True
        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0:
                    finish_loof = False

print(time)
print(cnt)

#### 아래 방법으로 풀이하면 바깥에 있는 공기와 내부에 있는 공기의 구별이 힘들다. 

# def search(x, y, N, M):
#     global cnt 

#     ## 현재 지점은 다시 방문하지 않도록 값을 변경한다.
#     graph[x][y] = -1

#     ## 상, 하, 좌, 우
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if (0 <= nx < N) and (0 <= ny < M):
#             if graph[nx][ny] == 0:
#                 ## 공기와 맞닿는 부분이 존재할 때
#                 ## 그래프-카피의 경우 한시간 뒤 그래프의 상태를 그린다.
#                 ## 현재 그래프에서 상, 하, 좌, 우 중 한군데라도 공기와 맞닿아 있으므로 한시간뒤 그래프에서 현재 위치는 값이 0 이 될 것
#                 graph_copy[x][y] = 0
#             elif graph[nx][ny] > 0:
#                 cnt += 1
#                 search(nx, ny, N, M)
 
# ## 입력 및 그래프 생성
# N, M = map(int, sys.stdin.readline().split())

# graph = []
# for _ in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))

# graph_copy = []
# for i in range(0, len(graph)):
#     graph_copy.append(graph[i].copy())

# ## 결과
# time = 0
# finish_loof = False
# cnt = 0

# print(graph)

# ## 탐색
# while True:
#     if finish_loof:
#         break
#     else:
#         time += 1
#         cnt = 0

#         for i in range(N):
#             for j in range(M):
#                 if graph[i][j] > 0:
#                     search(i, j, N, M)
        
#         graph = []

#         for i in range(0, len(graph_copy)):
#             graph.append(graph_copy[i].copy())

#         print(graph)

#         finish_loof = True
#         for i in range(N):
#             for j in range(M):
#                 if graph[i][j] != 0:
#                     finish_loof = False

# print(time)
# print(cnt)