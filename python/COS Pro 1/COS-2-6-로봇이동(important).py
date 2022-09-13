#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    # 여기에 코드를 작성해주세요.
    move = {
        'L': [-1, 0],
        'R': [1, 0],
        'U': [0, 1],
        'D': [0, -1]
    }

    x, y = 0, 0

    for c in commands:
        dx, dy = move[c]
        x += dx
        y += dy

    return [x, y]

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")