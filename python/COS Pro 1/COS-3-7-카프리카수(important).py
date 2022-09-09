def solution(k):
    answer = []
    for i in range(1, k + 1):
        square_num = i * i
        divisor = 1
        while square_num // divisor != 0:
            front = square_num // divisor
            back = square_num % divisor
            divisor *= 10
            if back != 0 and front != 0:
                if front + back == i:
                    answer.append(i)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution 함수만 수정하세요.
k = 500
ret = solution(k)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")