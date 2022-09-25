from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def search(x, y, X, Y, visited, graph, distance):
    visited[x][y] = True

    que = deque()
    que.append((x, y))
    distance[x][y] = 0

    while que:
        a, b = que.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < X) and (0 <= ny < Y):
                if not visited[nx][ny] and graph[nx][ny] != -1:
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[a][b] + 1
            
                    if graph[nx][ny] == 2:
                        return distance[nx][ny]

                    que.append((nx, ny))
    return -1
def solution(Map, Max_row_length, Max_col_length, students, students_length):
    
    graph = [[0] * Max_col_length for _ in range(Max_row_length)]

    for i in range(Max_row_length):
        for j in range(Max_col_length):
            if Map[i][j] == "_":
                graph[i][j] = 0
            elif Map[i][j] == "#":
                graph[i][j] = -1
            elif Map[i][j] == "@":
                graph[i][j] = 2
    
    for i in range(students_length):
        x, y = students[i][0], students[i][1]
        graph[x][y] = 1

    visited = [[False] * Max_col_length for _ in range(Max_row_length)]
    distance = [[0] * Max_col_length for _ in range(Max_row_length)]

    answer = 0
    for i in range(Max_row_length):
        for j in range(Max_col_length):
            if not visited[i][j] and graph[i][j] == 1:
                answer += search(i, j, Max_row_length, Max_col_length, visited, graph, distance)
                visited = [[False] * Max_col_length for _ in range(Max_row_length)]

    return answer 

Max_row_length = 3
Max_col_length = 8
students = [[0, 1], [2, 7], [1, 6]]
studnets_length = len(students)
map = [
    ["_", "_", "#", "_", "_", "#", "_", "_"],
    ["_", "_", "#", "_", "@", "#", "_", "_"],
    ["_", "_", "_", "_", "_", "_", "_", "_"]
]


print(solution(map, Max_row_length, Max_col_length, students, studnets_length))