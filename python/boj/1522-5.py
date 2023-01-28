import sys
input = sys.stdin.readline

target = list(input().strip())
n = len(target)

a_cnt = 0
for i in range(n):
    if target[i] == 'a':
        a_cnt += 1

target += target
ans = 1000 * 1000 + 1
for i in range(n):
    b_cnt = 0
    for j in range(i, i + a_cnt):
        if target[j] == 'b':
            b_cnt += 1
    
    ans = min(ans, b_cnt)

print(ans)