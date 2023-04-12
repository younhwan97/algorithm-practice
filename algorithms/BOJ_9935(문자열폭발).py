import sys
input = sys.stdin.readline

# 입력
word = input().rstrip()
target = input().rstrip()

# 반복
stk = []
for ch in word:
    if ch != target[-1]:
        stk.append(ch)
    else:
        tmp = ch
        for i in range(len(target) - 1):
            if stk:
                tmp += stk.pop()
            else:
                break
        tmp = tmp[::-1]
        if tmp != target:
            stk += tmp

ans = "".join(stk)
if ans == "":
    print("FRULA")
else:
    print(ans)