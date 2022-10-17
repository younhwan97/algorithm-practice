import sys
input = sys.stdin.readline

answer = set()

def find(n, team, red, blue):
    if len(team) == n:
        answer.add(team)
        return

    for i in range(n):
        if check[i] == 0:
            if red + 1 <= n // 2:
                check[i] = 1
                find(n, team + "r")
            elif blue + 1 <= n // 2:
                check[i] = 2
                find(n, team + "b")
            check[i] = 0
            
def solve():
    # 입력
    n = int(input())
    graph = []
    for _ in range(n): graph.append(list(map(int, input().split())))

    check = [0] * n 

    find(n, "")

    print(answer)

    # value = 1000000000

    # for i in range(len(answer)):
    #     tmp_1 = 0
    #     tmp_2 = 0
    #     for j in range(n):
    #         for k in range(j + 1, n):
    #             if answer[i][j] == answer[i][k]:
    #                 if answer[i][j] == 1:
    #                     tmp_1 += graph[j][k]
    #                     tmp_1 += graph[k][j]
    #                 else:
    #                     tmp_2 += graph[j][k]
    #                     tmp_2 += graph[k][j]             
    #     value = min(value, abs(tmp_1 - tmp_2))

    #     if value == 0:
    #         break

    print(value)
solve()