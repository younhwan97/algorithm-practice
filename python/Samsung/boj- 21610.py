import sys
input = sys.stdin.readline

def get_dir(dir):
    if dir == 1:
        return 0, -1
    elif dir == 2:
        return -1, -1
    elif dir == 3:
        return -1 , 0
    elif dir == 4:
        return -1, 1
    elif dir == 5:
        return 0 , 1
    elif dir == 6:
        return 1, 1
    elif dir == 7:
        return 1, 0
    elif dir == 8:
        return 1, -1

def move(n, cloud, dir, cnt):
    new_cloud = set()
    dx, dy = get_dir(dir)

    for position in cloud:
        x, y = position
        
        for _ in range(cnt):
            x += dx
            y += dy

            if x == 0:
                x = n
            elif x == n + 1:
                x = 1
            
            if y == 0:
                y = n
            elif y == n + 1:
                y = 1

        new_cloud.add((x, y))
    return new_cloud

def water_copy(n, cloud, graph):
    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    up = []

    for position in cloud:
        x, y = position
        x -= 1
        y -= 1

        cnt = 0
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]

            if (0 <= nx < n) and (0 <= ny < n):
                if graph[nx][ny] >= 1:
                    cnt += 1
        
        up.append(cnt)
    return up

def solve():
    # 입력
    n, m = map(int, input().split())
    graph = []

    for _ in range(n): graph.append(list(map(int, input().split())))

    cmd = []
    for _ in range(m):
        dir, cnt = map(int, input().split())
        cmd.append((dir, cnt))

    # 초기 구름 생성
    cloud = set()
    cloud.add((n, 1))
    cloud.add((n, 2))
    cloud.add((n - 1, 1))
    cloud.add((n - 1, 2))

    # 명령어 수행
    for i in range(m):
        dir, cnt = cmd[i]

        # 구름 이동
        cloud = move(n, cloud, dir, cnt)

        # 비 내림
        for position in cloud:
            x, y = position
            x -= 1
            y -= 1
            graph[x][y] += 1

        # 물복사버그
        up = water_copy(n, cloud, graph)
        index = 0
        for position in cloud:
            x, y = position
            x -= 1
            y -= 1
            graph[x][y] += up[index]
            index += 1

        # 새로운 구름 생성
        new_cloud = set()
        for j in range(n):
            for k in range(n):
                if graph[j][k] >= 2 and (j + 1, k + 1) not in cloud:
                    new_cloud.add((j + 1, k + 1))
                    graph[j][k] -= 2
        
        cloud = new_cloud
    
    # 결과 출력
    ans = 0
    for i in range(n):
        ans += sum(graph[i])

    print(ans)

solve()