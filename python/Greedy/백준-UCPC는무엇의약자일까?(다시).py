import sys

## 입력
input = sys.stdin.readline

s = input().split()

ucpc = ['U', 'C', 'P', 'C']

ucpc_index = 0

for i in range(0, len(s)):

    for j in range(0, len(s[i])):
        if s[i][j] == ucpc[ucpc_index]:
            ucpc_index += 1

            if ucpc_index == 4:
                break
            
    if ucpc_index == 4:
        break
    
if ucpc_index == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")