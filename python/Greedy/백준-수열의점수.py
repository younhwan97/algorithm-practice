import sys
input = sys.stdin.readline

n = int(input())

arr_minus = list()
arr_plus = list()
arr_zero = list()

for _ in range(n):
    temp = int(input())

    if temp == 0:
        arr_zero.append(0)
    elif temp > 0:
        arr_plus.append(temp)
    else:
        arr_minus.append(temp)

## 점수
total = 0

## 마이너스 배열
arr_minus.sort()
while len(arr_minus) >= 2:
    total += (arr_minus[0] * arr_minus[1])
    del arr_minus[0]
    del arr_minus[0]

## 제로 배열 
while arr_zero and arr_minus:
    del arr_minus[0]
    del arr_zero[0]

## 플러스 배열
arr_plus.sort(reverse=True)
while len(arr_plus) >= 2:
    if arr_plus[0] != 1 and arr_plus[1] != 1:
        ## 플러스 배열의 경우 값이 1인 원소는 곱하는 것보다 더해주는 것이 이득
        total += (arr_plus[0] * arr_plus[1])
        del arr_plus[0]
        del arr_plus[0]
    else:
        break

## 나머지 값 처리
total += sum(arr_minus)
total += sum(arr_plus)

## 답
print(total)