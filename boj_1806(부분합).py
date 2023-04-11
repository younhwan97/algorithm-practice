import sys
input = sys.stdin.readline

# 입력
N, S = map(int, input().split())
arr = list(map(int, input().split()))
INF = 100_001

# 구간 찾기
left, right = 0, 0
ans = INF
current = arr[0]

while left + 1 < N:
    # 값 업데이트
    if current >= S:
        ans = min(ans, right - left + 1)
    
    if right + 1 == N or current >= S:
        current -= arr[left]
        left += 1
    elif left == right or current < S:
        right += 1
        current += arr[right]

if current >= S:
    ans = min(ans, right - left + 1)

if ans == 100_001:
    print(0)
else:
    print(ans)