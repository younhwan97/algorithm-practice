import sys
input = sys.stdin.readline

ans = 1000000000000

def dif(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)

def com(start, chicken, home, m, tmp):
    global ans

    # 종료 조건
    if len(tmp) == m:
        totalDif = 0

        for h in home:
            minDif = 100000
            for t in tmp:
                minDif = min(minDif, dif(h, t))

            totalDif += minDif

        ans = min(ans, totalDif)
        return

    for i in range(start, len(chicken)):
        if chicken[i] not in tmp:
            tmp.add(chicken[i])
            com(i + 1, chicken, home, m, tmp)
            tmp.remove(chicken[i])


def solve():
    # 입력
    n, m = map(int, input().split())
    graph = []
    for _ in range(n): graph.append(list(map(int, input().split())))

    chicken = []
    home = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                chicken.append((i, j))
            elif graph[i][j] == 1:
                home.append((i, j))

    # 치킨 집 조합 생성
    com(0, chicken, home, m, set())

    print(ans)

solve()