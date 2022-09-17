# 반복을 이용한 방법
def solution(arr, K):
    answer = 0
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                tot = arr[i] + arr[j] + arr[k]

                if tot % K == 0:
                    answer += 1
    return answer

# 재귀를 이용한 방법
result = []

def pick_number(cnt, K, number_cnt, used_number):
    ## 종료 조건
    if cnt == 3:
        temp = list()
        for i in range(len(used_number)):
            if used_number[i] != 0:
                temp.append(i)

        if (temp[0] + temp[1] + temp[2]) % K == 0 and (temp[0], temp[1], temp[2]) not in result:
            result.append((temp[0], temp[1], temp[2]))

        return
    
    ## 재귀
    for i in range(len(number_cnt)):
        if number_cnt[i] > used_number[i]:
            used_number[i] += 1
            pick_number(cnt + 1, K, number_cnt, used_number)
            used_number[i] -= 1

## soultion 3
def solution3(arr, K):
    cnt = [[0] * 100_001 for _ in range(K + 1)]

    for i in range(len(arr)):
        cnt[1][arr[i]] = 1

        for j in range(2, 0, -1):
            for k in range(100_001):
                if j == 1 and arr[i] == k:
                    continue
                
                if cnt[j][k] > 0: cnt[j + 1][k + arr[i]] += cnt[j][k]
    
    answer = 0
    for i in range(3, 100_001, 3):
        answer += cnt[3][i]

    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5, 6]

number_cnt = [0] * (max(arr) + 1)
used_number = [0] * (max(arr) + 1)
for i in range(len(arr)): number_cnt[arr[i]] += 1

K = 3

pick_number(0, K, number_cnt, used_number)

ret = solution3(arr, K)
print("solution 함수의 반환 값은 ", ret, " 입니다.")