def power(base, exponent):
    val = 1
    for i in range(exponent):
        val *= base
    return val

def solution(k):
    answer = []
    bound = power(10, k)
    for i in range(bound // 10, bound):
        current = i
        calculated = 0
        while current != 0:
            calculated += power(current % 10, k)
            current //= 10
        if calculated == i:
            answer.append(i)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
k = 3
ret = solution(k)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")