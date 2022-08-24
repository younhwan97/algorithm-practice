import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
re = list()

if arr[n - 1] < 0:
    print(-1)
else:
    k = n
    s = 1
    for i in range(n):
        if arr[i] > 0:
            re.append(k)
            k -= 1
        else:
            re.append(s)
            s += 1

    for i in range(len(re)):
        if i + 1 < len(re):
            print(re[i], end = ' ')
        else:
            print(re[i])