import sys, math
input = sys.stdin.readline

n = int(input())

dp = [0] * 100_001

dp[1] = 1

for i in range(2, len(dp)):
    temp = math.sqrt(i)

    if math.ceil(temp) == math.floor(temp):
        ## 특정 자연수의 제곱수인 경우
        dp[i] = 1
    else:
        temp = int(temp)
        dp[i] += 1
        ## 1 -> 1^2
        ## 2 -> 1^2 + 1^2
        ## 3 -> 1^2 + 1^2 + 1^2
        ## 4 -> 2^2
        ## 5 -> 2^2 + 1^2
        ## 7 -> 2^2 + 1^2 + 1^2 + 1^2
        ## 8 -> 2^2 + 2^2
        ## 9 -> 3^2
        ## 10 -> 3^2 + 1^2
        ## 11 -> 3^2 + 1^2 + 1^2
        ## 12 -> 3^2 + 1^2 + 1^2 + 1^2
        ## 13 -> 3^2 + 2^2