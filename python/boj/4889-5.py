import sys
input = sys.stdin.readline

def solve():
    num = 1
    while True:
        s = list(input().strip())

        ans = 0

        stack = []

        # 종료 조건
        if "-" in s:
            break
        
        for i in range(len(s)):
            if s[i] == "}" and not stack:
                ans += 1
                stack.append("{")
            elif s[i] == "}" and stack:
                stack.pop()
            else:
                stack.append("{")

        ans += len(stack) // 2

        print(str(num) + ". " + str(ans))
        num += 1

solve()