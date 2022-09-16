def solution(walls):
    answer = 0
    for i in range(len(walls)):
    	for j in range(i+1, len(walls)):
            area = 0
            if walls[i][1] < walls[j][1]:
                area = walls[i][1] * (walls[j][0] - walls[i][0])
            else:
                area = walls[j][1] * (walls[j][0] - walls[i][0])

            if answer < area:
                answer = area
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니, 위의 코드만 수정하세요.
walls = [[1, 4], [2, 6], [3, 5], [5, 3], [6, 2]]
ret = solution(walls)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")