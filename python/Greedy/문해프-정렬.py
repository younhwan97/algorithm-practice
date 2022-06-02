import time

## 사용자 입력
n, k = map(int, input('n과 k를 순서대로 입력하세요: ').split())
arr = list(map(int, input('n개의 카드를 입력하세요: ').split()))

## 시작 시간
start = time.time()

## 초기 카드 상태 
#### 오름차순으로 정렬이 불가능한 경우를 판별하기 위해 따로 저장
init_arr = list(arr)

## 최소로 뒤집는 횟수 
answer = 0

def sort_card(arr):
    ## 함수 호출에서 뒤집은 횟수
    count = 0

    for index in range(0, n):
        if index + k <= n and arr[index] > arr[index + 1]:
            ## 우측으로 k개를 뒤집을 수 있을때
            ## 오름차순 정렬을 해야하기 때문에 현재 리스트의 index 값보다 index + 1 값이 크면 카드를 뒤집는다. (그리드 알고리즘을 이용)
            temp = list()
            for i in range(0, k):
                temp.append(arr[index + i])
            ## k개의 요소를 저장한 임시 리스트를 뒤집는다.
            temp.reverse()
            ## 기존의 리스트에 뒤집은 리스트를 대체한다.
            arr[index: index+k] = temp
            count += 1

    return arr, count        

while True:
    if sorted(arr) == arr:
        ## 리스트가 정렬됐을 때
        break
    else:
        arr2, count = sort_card(arr)
        arr = arr2
        answer += count
        if arr == init_arr:
            ## 정렬 결과가 초기 카드 상태와 같다면 오름차순 정렬이 불가능한 것으로 판별
            answer = -1
            break

print(answer)
print("실행시간: " + str(round(time.time() - start, 4)) + "초")
