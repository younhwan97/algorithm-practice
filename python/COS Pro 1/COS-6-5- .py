def solution(board):
    coins = [[0 for c in range(4)] for r in range(4)]
    for i in range(4):
        for j in range(4):
            if i == 0 and j == 0:
                coins[i][j] = board[i][j]
            elif i == 0 and j != 0:
                coins[i][j] = board[i][j] + coins[i][j-1]
            elif i != 0 and j == 0:
                coins[i][j] = board[i][j] + coins[i-1][j]
            else:
                coins[i][j] = board[i][j] + max(coins[i][j], coins[i-1][j-1])
    answer = coins[3][3]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으면 위의 코드만 수정하세요.
board = [[6, 7, 1, 2], [3, 5, 3, 9], [6, 4, 5, 2], [7, 3, 2, 6]]
ret = solution(board)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")