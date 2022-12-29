import sys, heapq
input = sys.stdin.readline

def solve():
    t1, t2, n = map(int, input().split())

    order = []
    for _ in range(n):
        time, color, count = input().split()
        time = int(time)
        count = int(count)

        need = 0
        if color == "B":
            need = t1
            color = 1
        else:
            need = t2
            color = 2

        for i in range(0, count):
            heapq.heappush(order, (time + need * i, color))
            
    s = []
    j = []

    num = 1
    while order:
        time, color = heapq.heappop(order)

        if color == 1:
            s.append(num)
        else:
            j.append(num)
        num += 1

    print(len(s))
    for i in range(len(s)):
        print(s[i], end = " ")
    print()
    print(len(j))
    for i in range(len(j)):
        print(j[i], end = " ")
solve()