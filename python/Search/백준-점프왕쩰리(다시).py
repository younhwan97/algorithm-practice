import sys
sys.setrecursionlimit(10 ** 6)

def dfs(row, i, j, N):
    global can_reach_end

    if i == N and j == N:
        can_reach_end = True
        return 0
    elif i <= N and j <= N:
        if row[i][j] == 0: return 0
        dfs(row, i + row[i][j], j, N)
        dfs(row, i, j + row[i][j], N)
    elif i < 0 or j < 0:
        return 0
    elif i > N or j > N:
        return 0

N = int(input())
row = [[-1, -1, -1, -1]]

for _ in range(N):
    temp = list(map(int, input().split()))
    temp.insert(0, -1)
    row.append(temp)

can_reach_end = False

dfs(row, 1, 1, N)

if can_reach_end == True:
    print("HaruHaru")
else:
    print("Hing")