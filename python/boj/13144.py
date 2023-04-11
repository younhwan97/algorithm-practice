import sys
input = sys.stdin.readline

# 투포인터라고 생각을 했어야 하는 이유?
# (1 ≤ N ≤ 100,000) N의 범위를 봤을 때, 웬만한 알고리즘은 시간초과를 유발
# 사용 가능한 알고리즘은 O(N) = N or N * logN
# 자연스럽게 스택, 큐, 투포인터, 이분탐색 등등으로 생각

N = int(input())
arr = list(map(int, input().split()))

left, right = 0, 1
ans = 1
used = set()
used.add(arr[left])

while right < N:
    if arr[right] not in used:
        used.add(arr[right])
        ans += (right - left + 1)
        right += 1
    else:
        while True:
            if arr[left] == arr[right]:
                left += 1
                ans += (right - left + 1)
                right += 1
                break

            used.remove(arr[left])
            left += 1

print(ans)