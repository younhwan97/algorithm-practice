import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1]

## 탐색 메서드 정의
def search(x, y, cnt):
    global max_length

    max_length = max(cnt, max_length)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < R) and (0 <= ny < C):
            if result[graph[nx][ny]] == 0:
                ## 방문 체크
                result[graph[nx][ny]] = 1

                ## 재귀 탐색
                search(nx, ny, cnt + 1)

                ## 백트랙킹
                result[graph[nx][ny]] = 0

## 입력 및 그래프 생성
R, C = map(int, input().split())

graph = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(R)]
                
## 탐색
max_length = 0

result = [0] * 26
result[graph[0][0]] = 1

search(0, 0, 1)

print(max_length)