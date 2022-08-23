import sys
input = sys.stdin.readline

s = input().strip()
p = input().strip()

temp = ""
cnt = 1
for i in range(len(p)):
    temp += p[i]

    if temp not in s:
        temp = p[i]
        cnt += 1

print(cnt)