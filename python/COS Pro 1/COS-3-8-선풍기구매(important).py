def solution(k, student):
    answer = 0
    for s in student:
        s -= 4*k
        if s <= 0:
            continue ## break -> continue  / 놓치기 쉬울 듯
        answer += (s + k - 1) // k ## important / 몫을 구하기 위한 테크닉
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
k1 = 1
student1 = [4, 4, 4, 4]
ret1 = solution(k1, student1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

k2 = 3
student2 = [15, 17, 19, 10, 23]
ret2 = solution(k2, student2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")