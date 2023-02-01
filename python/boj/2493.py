import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stk = [(arr[0], 1)]
ans = [-1] * N
ans[0] = 0

for i in range(1, N):
    while stk:
        height, index = stk.pop()

        if height >= arr[i]:
            stk.append((height, index))
            stk.append((arr[i], i + 1))
            ans[i] = index
            break
    
    if ans[i] == -1:
        ans[i] = 0
        stk.append((arr[i], i + 1))
    
for value in ans:
    print(value, end = " ")