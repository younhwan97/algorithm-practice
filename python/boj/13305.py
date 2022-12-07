import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    distance = list(map(int, input().split()))
    price = list(map(int, input().split()))

    ##   2 . 3 . 1 . 4
    ## 5 . 5 . 4 . 3 . 5
    
    ans = 0
    target = price[0]
    for i in range(1, len(price)):
        ans += target * distance[i - 1]

        if price[i] < target:
             target = price[i]
    
    print(ans)

solve()