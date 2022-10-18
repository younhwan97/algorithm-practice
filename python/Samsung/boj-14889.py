import sys
input = sys.stdin.readline

ans = 100000000

def find(n, start, star_team, graph):
    global ans

    # 종료
    if len(star_team) == n // 2:
        ## 링크 팀 구성
        link_team = set()
        for i in range(n):
            if i not in star_team:
                link_team.add(i)

        star, link = 0, 0

        for i in star_team:
            for j in star_team:
                if i != j:
                    star += graph[i][j]

        for i in link_team:
            for j in link_team:
                if i != j:
                    link += graph[i][j]

        ans = min(ans, abs(star - link))
        return

    # 재귀
    ## 중복된 팀 구성을 피하기 위해 start 매개 변수 활용
    for i in range(start, n):
        if i not in star_team:
            star_team.add(i)
            find(n, i + 1, star_team, graph)
            star_team.remove(i)

def solve():
    # 입력
    n = int(input())
    graph = []
    for _ in range(n): graph.append(list(map(int, input().split())))

    # 시작
    find(n, 0, set(), graph)

    # 출력
    print(ans)

solve()