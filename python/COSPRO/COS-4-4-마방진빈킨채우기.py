def func_a(matrix):
    n = 4
    ret = []
    exist = [False for _ in range(n*n + 1)]
    for i in range(0, n):
        for j in range(0, n):
                exist[matrix[i][j]] = True
    for i in range(1, n*n+1):
        if exist[i] == False:
            ret.append(i)
    return ret

def func_b(matrix):
    n = 4
    ret = []
    for i in range(0, n):
        for j in range(0, n):
            if matrix[i][j] == 0:
                ret.append([i, j])
    return ret

def func_c(matrix):
    n = 4
    goal_sum = sum(range(1, n*n+1))//n
    for i in range(0, n):
        row_sum = 0
        col_sum = 0
        for j in range(0, n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]
        if row_sum != goal_sum or col_sum != goal_sum:
            return False

    main_diagonal_sum = 0
    skew_diagonal_sum = 0
    for i in range(0, n):
        main_diagonal_sum += matrix[i][i]
        skew_diagonal_sum += matrix[i][n-1-i]
    if main_diagonal_sum != goal_sum or skew_diagonal_sum != goal_sum:
        return False
    return True

def solution(matrix):
    answer = []
    coords = func_b(matrix)
    nums = func_a(matrix)

    matrix[coords[0][0]][coords[0][1]] = nums[0]
    matrix[coords[1][0]][coords[1][1]] = nums[1]
    if func_c(matrix):
        for i in range(0, 2):
            answer.append(coords[i][0] + 1)
            answer.append(coords[i][1] + 1)
            answer.append(nums[i])
    else:
        matrix[coords[0][0]][coords[0][1]] = nums[1]
        matrix[coords[1][0]][coords[1][1]] = nums[0]
        for i in range(0, 2):
            answer.append(coords[1-i][0] + 1)
            answer.append(coords[1-i][1] + 1)
            answer.append(nums[i])
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
matrix = [[16,2,3,13],[5,11,10,0],[9,7,6,12],[0,14,15,1]]
ret = solution(matrix)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")