import sys
input = sys.stdin.readline

x, y = map(int, input().split())
turn = (x + y) * 2

value = 1
while True:
    if value * (value + 1) == turn:
        turn = value
        break
    elif value * (value + 1) > turn:
        turn = -1
        break
    else:
        value += 1

if turn == -1:
    print(-1)
else:
    a = 0
    b = 0
    cnt = 0
    for i in range(turn, 0, -1):
        if a + i <= x:
            a += i
            cnt += 1
        else:
            b += i

    print(cnt)