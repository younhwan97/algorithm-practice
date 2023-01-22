import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keyword = set()

for _ in range(N):
    keyword.add(input().strip())

for _ in range(M):
    written = list(input().strip().split(','))

    for i in range(len(written)):
        if written[i] in keyword:
            keyword.remove(written[i])

    print(len(keyword))