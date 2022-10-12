#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(bishops):
    #여기에 코드를 작성해주세요.

    a = [[0] * 9 for _ in range(9)]

    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]

    for i in range(len(bishops)):
        position = bishops[i]

        x = ord(position[0]) - ord('A')
        y = int(position[1]) - 1

        for j in range(4):
            for step in range(0, 9):
                nx = x + step * dx[j]
                ny = y + step * dy[j]
                if (0 <= nx < 8) and (0 <= ny < 8):
                    a[nx][ny] = 1
                else:
                    break

    cnt = 0
    for i in range(1, 9):
        for j in range(1, 9):
            if a[i][j] == 0:
                cnt += 1

    answer = cnt
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
bishops1 = ["D5"]
ret1 = solution(bishops1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

bishops2 = ["D5", "E8", "G2"]
ret2 = solution(bishops2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")