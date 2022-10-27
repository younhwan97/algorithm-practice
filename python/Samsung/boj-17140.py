import sys, heapq
input = sys.stdin.readline

def r_function(graph, r, c):
    check = [[0] * 101 for _ in range(r)]

    for i in range(r):
        for j in range(c):
            value = graph[i][j]
            check[i][value] += 1
    
    max_row_cnt = -1

    for i in range(r):
        cnt = 0
        for j in range(1, 101):
            if check[i][j] != 0:
                cnt += 1
        max_row_cnt = max(max_row_cnt, cnt)
    
    max_row_cnt *= 2
    
    new_graph = [[0] * max_row_cnt for _ in range(r)]

    for i in range(r):
        pq = []
        for j in range(1, 101):
            if check[i][j] != 0:
                heapq.heappush(pq, (check[i][j], j))

        idx = 0
        while pq:
            cnt, value = heapq.heappop(pq)

            new_graph[i][idx] = value
            idx += 1
            new_graph[i][idx] = cnt
            idx += 1

    return new_graph

def c_function(graph, r, c):
    check = [[0] * 101 for _ in range(c)]

    for i in range(r):
        for j in range(c):
            value = graph[i][j]
            check[j][value] += 1
    
    max_col_cnt = -1

    for i in range(c):
        cnt = 0
        for j in range(1, 101):
            if check[i][j] != 0:
                cnt += 1
        max_col_cnt = max(max_col_cnt, cnt)

    max_col_cnt *= 2
    
    new_graph = [[0] * c for _ in range(max_col_cnt)]

    for i in range(c):
        pq = []
        for j in range(1, 101):
            if check[i][j] != 0:
                heapq.heappush(pq, (check[i][j], j))

        idx = 0
        while pq:
            cnt, value = heapq.heappop(pq)
            new_graph[idx][i] = value
            idx += 1
            new_graph[idx][i] = cnt
            idx += 1
    
    return new_graph

def solve():
    r, c, k = map(int, input().split())
    row = 3
    col = 3

    graph = []
    for _ in range(3): 
        graph.append(list(map(int, input().split())))

    ans = 0
    while True:
        if (row >= r and col >= c and graph[r - 1][c - 1] == k ) or ans > 100:
            break
            
        ans += 1

        if row >= col:
            graph = r_function(graph, row, col).copy()
            col = len(graph[0])
        else:
            graph= c_function(graph, row, col).copy()
            row = len(graph)

    if ans == 101:
        print(-1)
    else:
        print(ans)

solve()