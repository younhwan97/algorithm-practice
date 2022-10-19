import sys, heapq
input = sys.stdin.readline

def check(graph, n, x, y, friends):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    friend = 0
    blank = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if graph[nx][ny] == 0:
                blank += 1
            elif graph[nx][ny] in friends:
                friend += 1
    return friend, blank

def solve():
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    info = []
    friend = [[] for _ in range(n * n + 1)]
    for i in range(n * n):
        info.append(list(map(int, input().split())))
    
    # 시작
    for i in range(len(info)):
        tmp = info[i] 
        target = tmp[0]
        friends = [tmp[1], tmp[2], tmp[3], tmp[4]]
        friend[target] = friends

        pq = []
        for j in range(n):
            for k in range(n):
                f, b = check(graph, n, j, k, friends)
                heapq.heappush(pq, (-1 * f, -1 * b, j, k))

        while pq:
            f, b, x, y = heapq.heappop(pq)
            if graph[x][y] == 0:
                graph[x][y] = target
                break

    # 만족도 구하기
    answer = 0
    for i in range(n):
        for j in range(n):
            a, b = check(graph, n, i, j, friend[graph[i][j]])
            if a != 0:
                answer += (10 ** (a - 1))
    
    # 결과 출력
    print(answer)

solve()