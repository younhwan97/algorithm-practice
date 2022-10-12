def solution(n):
    answer = ''
    for i in range(n):
        answer += str(i % 9 + 1)
        answer = answer[::-1]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n = 7  
ret = solution(n)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")