n = int(input())
arr = list(map(int, input().split()))

dp = [-1000] * (100_001)

## dp 리스트의 첫번째, 두번째 원소를 초기화
dp[1] = arr[0]
if arr[1] < 0:
    dp[2] = arr[0]
else:
    dp[2] = arr[1] + arr[0] 

## 10 -4 3 1 5 6 -35 12 21 -1
## 1 = 10 (arr[0])
## 2 = 10 (arr[0])
## 3 = 10 (arr[0])
## 4 = 10 (arr[0])
## 5 = 15 (arr[0] + .. + arr[4]])
## .. 
## 8 = 21 
## 9 = 33 (arr[7] + arr[8])

for i in range(3, len(arr)):
    dp[i] = max(dp[i - 1] + arr[i - 1], arr[i - 1])

print(max(dp))