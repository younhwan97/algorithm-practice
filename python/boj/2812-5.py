import sys
input = sys.stdin.readline

# 스택 이용하는 문제 공부할 것!

def solve():
    n, k = map(int, input().split())
    m = n - k
    num = list(map(int, list(input().strip())))

    stack = []
    for i in range(0, len(num)):
        value = num[i]

        while stack and k > 0:
            v = stack.pop()
            k -= 1

            if v >= value:
                stack.append(v)
                k += 1
                break
        
        if len(stack) < m:
            stack.append(value)

    print("".join((str(c) for c in stack)))
    
solve()