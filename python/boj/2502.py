import sys
input = sys.stdin.readline

D, K = map(int, input().split())
dp = [[True] * (K + 1) for _ in range(D)]

def go(index, a, b):
    global D, dp

    if index == D:
        return True

    if not dp[index][b]: return False

    tmp = a - b

    if tmp > 0:
        dp[index][b] = go(index + 1, b, tmp)
    else:
        return False
    
    return dp[index][b]

first, second = K, -1
for i in range(K - 1, -1, -1):
    if K - i < i:
        res = go(1, K, i)

        if res:
            second = i
            break

index = 2
while first > 0 and second > 0:
    if index == D:
        break

    tmp = first - second
    first = second
    second = tmp
    index += 1

print(second)
print(first)