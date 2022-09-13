#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(enemies, armies):
	answer = 0
	enemies.sort()
	armies.sort()
	i, j = 0, 0
	while i < len(enemies) and j < len(armies):
		if enemies[i] <= armies[j]:
			answer = answer + 1
			i = i + 1
			j = j + 1
		else:
			j = j + 1
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
enemies1 = [1, 4, 3]
armies1 = [1, 3]
ret1 = solution(enemies1, armies1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

enemies2 = [1, 1, 1]
armies2 = [1, 2, 3, 4]
ret2 = solution(enemies2, armies2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")