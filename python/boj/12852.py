import sys
input = sys.stdin.readline

N = int(input())
dp = [N] * (N + 1)
dp[0], dp[1] = 0, 0
ans = []

for i in range(2, N + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i - 1 >= 1:
        dp[i] = min(dp[i], dp[i - 1] + 1)

result = []
def search(cnt, value, ans):
    global N, dp, result

    if cnt == 0:
        result = ans.copy()
        return

    for i in range(N):
        if cnt - 1 == dp[i]:
            if (value % 3 == 0 and value // 3 == i) or (value % 2 == 0 and value // 2 == i) or value - 1 == i:
                ans.append(i)
                search(cnt - 1,i, ans)
                ans.pop()
        
        if result:
            break

ans = [N]
search(dp[-1], N, ans)

print(len(result) - 1)

for i in result:
    print(i, end = " ")

# def go(value, cnt):
#     global N, dp

#     if value == 1:
#         return 1

#     if dp[value] != 0:
#         return dp[value] + cnt
    
#     cnt1 = N
#     if value % 3 == 0:
#         cnt1 = 0
#         cnt1 = go(value // 3, cnt1 + 1)

#     cnt2 = N
#     if value % 2 == 0:
#         cnt2 = 0
#         cnt2 = go(value // 2, cnt2 + 1)

#     cnt3 = N
#     if value - 1 >= 1:
#         cnt3 = 0
#         cnt3 = go(value - 1, cnt3 + 1)

#     dp[value] = min(cnt1, cnt2, cnt3)
#     return dp[value] + cnt

# cnt = go(N, 0)

# print(dp)
# print(cnt)
