import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    target = list(input().strip())

    tmp = 0
    
    # 파란 공을 움직일 때
    ## 파란 공을 왼쪽으로 모을 때
    blue_left = 0

    for c in target: ## RBBBRBRRR
        if c == 'R':
            tmp += 1
        else:
            if tmp > 0:
                blue_left += 1

    tmp = 0

    ## 파란 공을 오른쪽으로 모을 때
    blue_right = 0

    for i in range(len(target) - 1, -1, -1):
        if target[i] == 'R':
            tmp += 1
        else:
            if tmp > 0:
                blue_right += 1
    
    tmp = 0

    # 빨간 공을 움직일 때
    ## 빨간 공을 왼쪽으로 모을 때
    red_left = 0

    for c in target: ## RBBBRBRRR
        if c == 'B':
            tmp += 1
        else:
            if tmp > 0:
                red_left += 1

    tmp = 0

    ## 빨간 공을 오른쪽으로 모을 때
    red_right = 0

    for i in range(len(target) - 1, -1, -1):
        if target[i] == 'B':
            tmp += 1
        else:
            if tmp > 0:
                red_right += 1
    
    ans = min(min(blue_left, blue_right), min(red_left, red_right))
    print(ans)

solve()