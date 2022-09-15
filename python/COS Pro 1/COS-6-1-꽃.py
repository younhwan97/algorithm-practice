#다음과 같이 import를 사용할 수 있습니다.
#import math

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, n, garden, visited, result):
    visited[x][y] = True
    result[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if not visited[nx][ny] and garden[nx][ny] == 1:
                dfs(nx, ny, n, garden, visited, result)
            elif garden[nx][ny] == 0:
                result[nx][ny] = 1
            
def solution(n, garden):
    #여기에 코드를 작성해주세요.
    answer = 0

    while True:
        ## 아직 피지 않은 꽃이 있는지 확인
        finish_loof = True
        for i in range(n):
            for j in range(n):
                if garden[i][j] == 0:
                    finish_loof = False
                    break
            if not finish_loof:
                break
        
        if finish_loof:
            break

        ## 탐색
        visited = [[False] * n for _ in range(n)] 
        result = [[0] * n for _ in range(n)]
        answer += 1
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and garden[i][j] == 1:
                    dfs(i, j, n, garden, visited, result)
        
        garden = result[:]
            
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")