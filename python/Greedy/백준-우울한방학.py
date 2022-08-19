import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

temp = m - (sum(arr) + n)

if 0 < temp <= n:
    print(temp)
elif temp <= 0 :
    print(0)
else:
    result = [1] * (n + 1)

    temp -= (n + 1)

    index = 0
    while temp > 0:
        result[index] += 1
        index += 1
        temp -= 1

        if index == n + 1:
            index = 0
    
    cost = 0
    for i in range(0, len(result)):
        for j in range(1, result[i] + 1):
            cost += (j * j)
    
    print(cost)