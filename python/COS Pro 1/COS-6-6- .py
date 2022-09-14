def solution(grid):
    answer = 0
    for i in range(4):
        for j in range(4):
            for k in range(j + 1, 4, 2):
                answer = max(answer, max(grid[i][j] + grid[j][k], grid[j][k] + grid[k][i]))
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
grid = [[1, 4, 16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]]
ret = solution(grid)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")