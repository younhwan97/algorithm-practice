import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

ans = 0

def check(a, b):
    global ans

    if a == b:
        ans = 1
        return

    if len(b) <= len(a):
        return

    if ans == 0:
        if b[0] == 'A' and b[-1] == 'B':
            ans = 0
            return
    
    if b[0] == 'A':
        check(a, b[:-1])
    else:
        if b[-1] == 'A':
            check(a, b[:-1])
            check(a, b[1:][::-1])
        else:
            check(a, b[1:][::-1])

a = input().strip()
b = input().strip()

check(a, b)
print(ans)