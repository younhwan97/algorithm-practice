#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(number, target):
    #여기에 코드를 작성해주세요.
    dp = [-1] * 10_001

    dp[number] = 0

    for i in range(number + 1, target + 1):
        dp[i] = dp[i - 1] + 1

        if (i + 1) % 2 == 0 and dp[(i + 1) // 2] != -1:
            dp[i] = min(dp[i], dp[(i + 1) // 2] + 2)
        
        if i % 2 == 0 and dp[i // 2] != -1:
            dp[i] = min(dp[i], dp[i // 2] + 1)
            
    answer = dp[target]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
number1 = 6
target1 = 11
ret1 = solution(number1, target1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 3
target2 = 11
ret2 = solution(number2, target2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")