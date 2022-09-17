#다음과 같이 import를 사용할 수 있습니다.
#import math

## 반복을 이용한 방법
def solution(arr, K):
    #여기에 코드를 작성해주세요.
    answer = 0

    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                tot = arr[i] + arr[j] + arr[k]

                if tot % K == 0:
                    answer += 1

    return answer

## 재귀를 이용한 방법
result = []
def pick_number(cnt, K, number_cnt, used_number):
    if cnt == 3:
        temp = list()
        for i in range(len(used_number)):
            if used_number[i] != 0:
                temp.append(i)

        if (temp[0] + temp[1] + temp[2]) % K == 0 and (temp[0], temp[1], temp[2]) not in result:
            result.append((temp[0], temp[1], temp[2]))
            
        return

    for i in range(len(number_cnt)):
        if number_cnt[i] > used_number[i]:
            used_number[i] += 1
            pick_number(cnt + 1, K, number_cnt, used_number)
            used_number[i] -= 1
    
#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]

number_cnt = [0] * (max(arr) + 1)
used_number = [0] * (max(arr) + 1)
for i in range(len(arr)): number_cnt[arr[i]] += 1

K = 3

pick_number(0, K, number_cnt, used_number)
print(len(result))

# ret = solution(arr, K)
#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
# print("solution 함수의 반환 값은 ", ret, " 입니다.")