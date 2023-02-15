import sys
input = sys.stdin.readline

dp = [-1] * 91
dp[0] = 0
dp[1] = 1

def go(index):
    if dp[index] != -1:
        return dp[index]

    dp[index] = go(index - 1) + go(index - 2)
    return dp[index]

n = int(input())

print(go(n))