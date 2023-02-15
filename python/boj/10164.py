import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

dp1 = [[0] * m for _ in range(n)]
dp2 = [[0] * m for _ in range(n)]

row = k // m

if k % m == 0:
    row -= 1

col = k - row * m - 1

def go1(x, y):
    global n, m, row, col

    if dp1[x][y] != 0:
        return dp1[x][y]

    if x == row and y == col:
        return 1

    # 오른쪽
    n1 = 0
    if y + 1 < m:
        n1 = go1(x, y + 1)

    # 아래쪽 
    n2 = 0   
    if x + 1 < n:
        n2 = go1(x + 1, y)

    dp1[x][y] = n1 + n2
    return dp1[x][y]

def go2(x, y):
    global n, m

    if dp2[x][y] != 0:
        return dp2[x][y]
    
    if x == n - 1 and y == m - 1:
        return 1
    
    # 오른쪽
    n1 = 0
    if y + 1 < m:
        n1 = go2(x, y + 1)

    # 아래쪽 
    n2 = 0   
    if x + 1 < n:
        n2 = go2(x + 1, y)

    dp2[x][y] = n1 + n2
    return dp2[x][y]

ans = -1
if k != 0:
    ans = go1(0, 0) * go2(row, col)
else:
    ans = go2(0, 0)
print(ans)