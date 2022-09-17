def solution(K, numbers, up_down):
    left = 1
    right = K
    for num, word in zip(numbers, up_down):
        if word == "UP":
            left = num + 1 if left < num else left
        elif word == "DOWN":
            right = num - 1 if right > num else right
        elif word == "RIGHT":
            return 1
    return right - left + 1

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K1 = 10
numbers1 = [4, 9, 6]
up_down1 = ["UP", "DOWN", "UP"]
ret1 = solution(K1, numbers1, up_down1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")