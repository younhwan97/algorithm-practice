import sys

N = int(sys.stdin.readline())
arr = [0] * 301

index = 1
for _ in range(N):
    value = int(sys.stdin.readline())
    arr[index] = value
    index += 1

dp = [0] * (301)
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for i in range(3, N + 1):
    ## i - 1 번째 계단을 밟았을 때
    temp = arr[i - 1] + dp[i - 3] + arr[i]

    ## i - 1 번째 계단을 밟지 않았을 때 
    temp2 = dp[i - 2] + arr[i]

    if temp > temp2:
        dp[i] = temp
    else:
        dp[i] = temp2
    
print(dp[N])