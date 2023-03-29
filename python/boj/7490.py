N = int(input())

# 시간복잡도
## 완전탐색, 각 단계에서 결정할 수 있는 경우의수 -> 3
## 최대 깊이는 9, 고로 O(N) = 3^9 * T = 196,830 <= 1s
### 시작 복잡도 잘 고려해서 풀자!

operation = ["+", "-", " "]
ans = []

def go(now, n, oper):
    oper += str(now)

    if now == n:
        tmp = oper.replace(" ", "")
        if eval(tmp) == 0:
            ans.append(oper)
        return
    
    for i in range(3):
        go(now + 1, n, oper + operation[i])

for _ in range(N):
    n = int(input())

    for i in range(3):
        go(2, n, "1" + operation[i])

    ans.sort()
    for o in ans:
        print(o)

    ans.clear()

    print()