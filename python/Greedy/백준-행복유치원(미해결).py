import sys

## 입력
input = sys.stdin.readline

N, K = map(int, input().split())
height = list(map(int, input().split()))

diff = []
for i in range(1, N):
    diff.append(height[i] - height[i - 1])
diff.sort()

print(diff)
# answer = 0
# for i in range(N-K):
#     answer += diff[i]
# print(answer)