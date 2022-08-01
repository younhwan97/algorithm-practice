import sys

## 입력
n, E, W, N, S = map(int, sys.stdin.readline().split())

## 탐색 메서드 정의
def search(x, y, per, length):
    if length >= n:
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    prob = [E, W, N, S]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        p = prob[i]

        if (0 <= nx < 2 * n + 1) and (0 <= ny < 2 * n + 1):
            if visitied[nx][ny] == False:
                if x == n and y == n:
                    percentage[nx][ny] = 1
                    visitied[nx][ny] = True
                    search(nx, ny, 1, 1)
                else:
                    length += 1
                    per = per * (p / 100)
                    percentage[nx][ny] = per
                    visitied[nx][ny] = True
                    search(nx, ny, per, length)
                
## 탐색
percentage = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
percentage[n][n] = 0

visitied = [[False] * (2 * n + 1) for _ in range(2 * n + 1)]
visitied[n][n] = True
search(n, n, 1, 0)

for i in range(0, len(percentage)):
    print(percentage[i])