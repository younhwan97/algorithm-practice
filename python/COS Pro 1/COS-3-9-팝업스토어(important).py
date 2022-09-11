def solution(revenue, k) :
    answer = 0
    rsum = sum(revenue[0:k])
    answer = rsum
    for i in range(k, len(revenue)) :
        rsum = rsum - revenue[i - k] + revenue[i]
        if answer < rsum :
            answer = rsum
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래 코드는 잘못된 부분이 없으니, solution함수만 수정하세요.
revenue1 = [1, 1, 9, 3, 7, 6, 5, 10]
k1 = 4
ret1 = solution(revenue1, k1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

revenue2 = [1, 1, 5, 1, 1]
k2 = 1
ret2 = solution(revenue2, k2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")