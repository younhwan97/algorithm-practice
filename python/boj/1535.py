import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
dp = [[0] * 101 for _ in range(21)]

def go(index, total, value):
    global dp, n

    if dp[index][total] != 0:
        return dp[index][total] + value
    
    if index == n:
        return value
    
    n1 = 0
    if total + arr1[index] <= 99:
        n1 = go(index + 1, total + arr1[index], arr2[index])

    n2 = go(index + 1, total, 0)

    dp[index][total] = max(n1, n2)
    return dp[index][total] + value

print(go(0, 0, 0))