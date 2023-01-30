import sys
input = sys.stdin.readline

target = list(input().strip())
stk = []
while target:
    word = target.pop()

    if word == ")":
        stk.append(")")
    elif word == "(":
        value = 0
        cnt = target.pop()
        while True:
            tmp = stk.pop()
            if tmp == ")":
                break
            else:
                value += tmp
        stk.append(int(cnt) * value)
    else:
        stk.append(1)

ans = 0
while stk:
    ans += int(stk.pop())
print(ans)