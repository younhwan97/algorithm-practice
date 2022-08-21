import sys
input = sys.stdin.readline

n = int(input())
a = [0] * n
b = list(map(int, input().split()))

cnt = 0
while True:
    if a == b:
        print(cnt)
        break
    else:
        cnt += 1

        can_twice = True

        for i in range(len(b)):
            if b[i] % 2 != 0:
                b[i] -= 1
                can_twice = False
                break
        
        if can_twice:
            for i in range(len(b)):
                b[i] = b[i] // 2