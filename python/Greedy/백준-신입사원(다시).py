import sys

T = int(sys.stdin.readline())

for _ in range(T):
    people = list()

    N = int(sys.stdin.readline())
    for _ in range(N):
        paper, interview = map(int, sys.stdin.readline().split())
        people.append([paper, interview])
    
    people.sort()

    cnt = 1
    max = people[0][1]
    for i in range(1, N):
        if max > people[i][1]:
            cnt += 1
            max = people[i][1]
    
    print(cnt)