import sys
input = sys.stdin.readline

N, K, P, X = map(int, input().split())
X = str(X)
numbers = [
    "1111110",
    "0011000",
    "0110111",
    "0111101",
    "1011001",
    "1101101",
    "1101111",
    "0111000",
    "1111111",
    "1111101"
]

def atob(a, b):
    global numbers

    cnt = 0

    if a == '.':
        for i in range(7):
            if numbers[b][i] == 1:
                cnt += 1
        return cnt

    for i in range(7):
        if numbers[a][i] != numbers[b][i]:
            cnt += 1
    
    return cnt

def go(index, cnt):
    global N, K, P, X

    if index == K or cnt == P: return 1
    
    ans = 0

    for i in range(10):
        need = atob(int(X[index]), i)
        if cnt + need <= P:
            tmp = X[:index] + str(i) + X[index + 1:]
            if int(tmp) <= N:
                ans += go(index + 1, cnt + need)
           
    return ans

dif = K - len(X)
for i in range(dif):
    X = "." + X

print(go(0, 0) - K)