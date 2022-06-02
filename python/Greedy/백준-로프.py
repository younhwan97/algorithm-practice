## 사용자 입력
n = int(input())
arr = list()

for i in range(0, n):
    arr.append(int(input()))

## 버틸 수 있는 최대 무게
answer = 0

## 배열을 내림차순 정렬
#### 버틸 수 있는 무게가 가장 큰 로프부터 정렬됨
arr.sort(reverse=True)

for index, item in enumerate(arr):
    ## 버틸 수 있는 무게가 가장 큰 로프부터 더 작은 로프를 추가하며 무게가 어떻게 변하는지 확인
    new_maximum_weight = item * (index + 1)
    if new_maximum_weight >= answer:
        answer = new_maximum_weight

print(answer)