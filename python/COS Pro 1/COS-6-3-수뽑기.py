#다음과 같이 import를 사용할 수 있습니다.
#import math

result = []

def pick_number(cnt, k, numbers, used_nunber):
    ## 종료조건
    if cnt == k:
        min_value = 0
        max_value = 0

        for i in range(len(used_nunber)):
            if used_nunber[i] != 0:
                min_value = i
                break
        
        for i in range(len(used_nunber) - 1, -1, -1):
            if used_nunber[i] != 0:
                max_value = i
                break

        if max_value - min_value not in result:
            result.append(max_value - min_value)

        return

    ## 재귀
    for i in range(len(numbers)):
        if numbers[i] > used_nunber[i]:
            used_nunber[i] += 1
            pick_number(cnt + 1, k, numbers, used_nunber)
            used_nunber[i] -= 1

def solution(arr, K):
    #여기에 코드를 작성해주세요.
    number = [0] * (max(arr) + 1)
    used_number = [0] * (max(arr) + 1)
    for i in range(len(arr)): number[arr[i]] += 1

    pick_number(0, K, number, used_number)

    return min(result)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [9, 11, 9, 6, 4, 19]
K = 4
ret = solution(arr, K)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")