import sys
input = sys.stdin.readline

# 줄 세우기 문제는 보통 전부다 옮겨 줄 필요는 없음
# -> 자신의 위치에 있지 않고, 다른 위치에 있는 대상만 옮겨주면 됨
# -> 해당 문제에서는 가장 긴 증가하는 부분수열을 구하고, 전체에서 빼주면 됨

N = int(input())
arr = list()
for _ in range(N):
    arr.append(int(input()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))