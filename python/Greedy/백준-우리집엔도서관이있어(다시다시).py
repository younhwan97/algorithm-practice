import sys

## 입력
input = sys.stdin.readline

n = int(input())
book = list()

for _ in range(n): book.append(int(input()))

cnt = 0
target = n 

## 핵심은 리스트를 실제로 변경할 필요가 없다는 것
for i in range(n):
    if book[n - 1 - i] == target:
        target -= 1
    else:
        cnt += 1

print(cnt)