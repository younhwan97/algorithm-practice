import sys

input = sys.stdin.readline

t = int(input())

dp = [0] * 68

dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

def new_fibo(num):
    if dp[num] != 0:
        return dp[num]
    
    dp[num] = new_fibo(num - 1) + new_fibo(num - 2) + new_fibo(num - 3) + new_fibo(num - 4)
    return dp[num]

for i in range(4, 68):
    new_fibo(i)

for _ in range(t):
    n = int(input())
    print(dp[n])