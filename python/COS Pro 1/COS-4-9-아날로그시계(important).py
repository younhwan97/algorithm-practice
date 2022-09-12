# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(hour, minute):
    # 분침
    m = (360 / 60) * minute

    # 시침
    h = (360 / 12) * hour + (360/12/60) * minute

    answer = round(abs(h - m), 1) if abs(h - m) < 180 else round(360 - abs(h-m), 1)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
hour = 2
minute = 50
ret = solution(hour, minute)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")