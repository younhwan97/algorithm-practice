import sys
sys.setrecursionlimit(10 ** 6)

## 입력 및 그래프 생성
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n): graph.append(list(input().split()))

## 탐색 메서드 정읜
dx = [1, 0]
dy = [0, 1]

def search(x, y, value):
    global max_ans
    global min_ans

    if x + 1 == n and y + 1 == n:
        max_ans = max(max_ans, eval(value))
        min_ans = min(min_ans, eval(value))
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny]:
                visited[nx][ny] = True

                if graph[nx][ny] == '+' or graph[nx][ny] == '-' or graph[nx][ny] == '*':
                    if x != 0 and y != 0:
                        temp = str(eval(value))
                        search(nx, ny, temp + graph[nx][ny])
                    else:
                        search(nx, ny, value + graph[nx][ny])
                else:
                    search(nx, ny, value + graph[nx][ny])

                visited[nx][ny] = False

max_ans = -1 * 100_000_000
min_ans = 100_000_000

visited = [[False] * n for _ in range(n)]
visited[0][0] = True

search(0, 0, graph[0][0])

for i in range(2):
    if i == 0:
        print(max_ans, end = ' ')
    else:
        print(min_ans)