import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def is_marble(graph, n, m):
    # 파란, 빨간 공의 존재 유무를 확인
    blue = False
    red = False

    for i in range(1, n -  1):
        for j in range(1, m - 1):
            if graph[i][j] == 'R':
                red = True

            if graph[i][j] == 'B':
                blue = True
        if blue and red:
            break
    return blue, red

# 방향
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move(dir, graph, n, m):
    moving = True

    while True:
        # 빨강, 파랑 공이 전혀 움직이지 않았으면 종료
        if not moving:
            break
        
        # 움직일 수 있는 공을 '방향'으로 계속 움직인다.
        moving = False
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if graph[i][j] == 'R' or graph[i][j] == 'B':
                    nx = i + dx[dir]
                    ny = j + dy[dir]

                    if (1 <= nx < n - 1) and (1 <= ny < m - 1):
                        if graph[nx][ny] == 'O':
                            # 공이 구멍으로 빠진다.
                            graph[i][j] = '.'
                            moving = True
                        elif graph[nx][ny] == '.':
                            # 공이 빈칸으로 이동한다.
                            graph[nx][ny] = graph[i][j]
                            graph[i][j] = '.'
                            moving = True

ans = 11

def find(cnt, graph, n, m, dir):
    global ans

    for i in dir:
        # 카피 그래프 생성
        graph_copy = []
        for j in range(n): graph_copy.append(graph[j].copy())

        # 이동
        move(i, graph_copy, n, m)

        # 공 확인
        blue, red = is_marble(graph_copy, n, m)

        if blue and not red:
            # 빨간 공만 빠져나왔을 때
            ans = min(ans, cnt)
        elif blue and red:
            # 파란 공, 빨간 공 둘다 아직 남아있을 때
            if cnt + 1 <= 10:
                ## 시행횟수가 10번 미만이라면
                new_dir = {0, 1, 2, 3}
                new_dir.remove(i)
                find(cnt + 1, graph_copy, n, m, new_dir)
        
def solve():
    global ans

    n, m = map(int, input().split())
    graph = []
    for _ in range(n): graph.append(list(input().strip()))

    # 브루트 포스
    find(1, graph, n, m, {0, 1, 2, 3})

    # 결과 출력
    if ans == 11:
        print(-1)
    else:
        print(ans)

solve()