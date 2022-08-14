import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

## 탐색 메서드 정의
def search(v, start):
    for i in graph[v]:
        if not visited[i]:
            if i == start:
                rel.add(start)
                for i in rel:
                    cycle[i] = True
            else:
                visited[i] = True
                rel.add(i)
                search(i, start)
                rel.remove(i)

## 입력
t = int(input())

## 테스트 케이스
for _ in range(t):
    ## 입력 및 그래프 생성
    n = int(input())
    arr = list(map(int, input().split()))

    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1): graph[i].append(arr[i - 1])

    ## 탐색
    cycle = [False] * (n + 1)
    for i in range(1, n + 1):
        if not cycle[i]:
            visited = [False] * (n + 1)
            rel = set()
            search(i, i)

    cnt = 0
    for i in range(1, n + 1):
        if not cycle[i]:
            cnt += 1

    print(cnt)