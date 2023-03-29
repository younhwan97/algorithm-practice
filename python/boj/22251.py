import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, K, P, X = map(int, input().split())
X = str(X)

# 자릿 수 맞춰주기!! 중요
if len(X) < K:
    for _ in range(K - len(X)):
        X = "0" + X

# 전광판 숫자를 문자열로 표현
numbers = [
    "0111111",
    "0001100",
    "1011011",
    "1011110",
    "1101100",
    "1110110",
    "1110111",
    "0011100",
    "1111111",
    "1111110"
]

check = [[0] * 10 for _ in range(10)]

# 숫자 a에서 b로 바꾸는데 몇개의 LED를 교체해야 하는지
def atob(a, b):
    cnt = 0
    for i in range(7):
        if numbers[a][i] != numbers[b][i]:
            cnt += 1

    check[a][b] = cnt
    check[b][a] = cnt
    return cnt

# 결과
ans = 0

# 탐색
def search(now, K, cnt, X, P, current, N):
    global ans

    if cnt > P: return

    if now == K:
        if 1 <= cnt:
            if 1 <= int(current) <= N:
                ans += 1
        return
    
    value = int(X[now])

    for i in range(0, 10):
        c = 0
        if check[value][i] != 0:
            c = check[value][i]
        else:
            c = atob(value, i)

        search(now + 1, K, cnt + c, X, P, current + str(i), N)

search(0, K, 0, X, P, "", N)
print(ans)