import sys
input = sys.stdin.readline

n = int(input())
limit = list(map(int, input().split()))

if limit[n - 1] < 0:
    print(-1)
else:
    sorted_arr = sorted(limit, reverse=True)
    result = [0] * n
    k = n
    j = 1
    for i in range(n):
        if limit[i] > 0:
            result[i] = k
            k -= 1
        else:
            result[i] = j
            j += 1

    print(result)