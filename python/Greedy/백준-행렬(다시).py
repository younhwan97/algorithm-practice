import sys

## 입력

input = sys.stdin.readline

N, M = map(int, input().split())

matrix_1 = []
matrix_2 = []

for i in range(2):
    for _ in range(N):
        temp = list(input().strip())
        temp = list(map(int, temp))

        if i == 0:
            matrix_1.append(temp)
        else:
            matrix_2.append(temp)

def change_matrix(x, y):
    for i in range(3):
        for j in range(3):
            if x + i < N and y + j < M:
                if matrix_1[x + i][y + j] == 1:
                    matrix_1[x + i][y + j] = 0
                else:
                    matrix_1[x + i][y + j] = 1
            
cnt = 0
for i in range(N - 3 + 1):
    for j in range(M - 3 + 1):
        if matrix_1[i][j] != matrix_2[i][j]:
            cnt += 1
            change_matrix(i, j)

            if matrix_1 == matrix_2:
                break
    if matrix_1 == matrix_2:
        break 

if matrix_1 == matrix_2:
    print(cnt)
else:
    print(-1)
