A, B = map(int, input().split())
answer = 0

while True:
    if A == B:
        break
    else:
        temp = A
        while True:
            if temp > B:
                A = A * 2
                break
            elif temp < B:
                temp = temp * 10 + 1
            else:
                A = B
                break
        