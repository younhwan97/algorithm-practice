import sys
from collections import deque

while True:
    ## 입력
    L, R, C = map(int, sys.stdin.readline().split())

    ## 종료 조건 확인
    if L == 0 and R == 0 and C == 0:
        break
    
    ## 그래프 생성
    graph_arr = []

    for i in range(L):
        graph = []
        
        for _ in range(R):
            temp = list(sys.stdin.readline().strip())
            graph.append(list(temp))

        sys.stdin.readline()

        graph_arr.append(graph)

    ## 시작 위치 찾기
    x = -1
    y = -1
    z = -1

    for i in range(0, len(graph_arr)):
        for j in range(0, len(graph_arr[i])):
            for k in range(0, len(graph_arr[i][j])):
                if graph_arr[i][j][k] == 'S':
                    x = j
                    y = k
                    z = i

                if x != -1 and y != -1 and z != -1:
                    break
            if x != -1 and y != -1 and z != -1:
                break
        if x != -1 and y != -1 and z != -1:
                break
    
    ## 탐색 메서드 정의
    def search(x, y, z):
        graph_arr[z][x][y] = 0

        ## 큐 생성
        que = deque()
        que.append((x, y, z))

        ## 반복
        while que:
            s, e, f, = que.popleft()

            ## 가능한 액션
            dx = [1, -1, 0, 0, 0, 0]
            dy = [0, 0, 1, -1, 0, 0]
            dz = [0, 0, 0, 0, 1, -1]

            for i in range(6):
                nx = s + dx[i]
                ny = e + dy[i]
                nz = f + dz[i]

                if (0 <= nx < R) and (0 <= ny < C) and (0 <= nz < L):
                    if graph_arr[nz][nx][ny] == '.':
                        que.append((nx, ny, nz))
                        graph_arr[nz][nx][ny] = graph_arr[f][s][e] + 1
                    elif graph_arr[nz][nx][ny] == 'E':
                        return graph_arr[f][s][e] + 1
    
    ## 탐색
    res = search(x, y, z)

    if res != None:
        print("Escaped in " + str(res) + " minute(s).")
    else:
        print("Trapped!")