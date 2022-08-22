import sys
input = sys.stdin.readline

n, x = map(int, input().split())

if x < n or n * 26 < x:
    print("!")
else:
    arr = [1] * n
    total = n 

    for i in range(n - 1, -1, -1):
        for j in range(26, 0, -1):
            total += (j - arr[i])
            arr[i] = j
        
            if total <= x:
                break
        if total == x:
            break

    for i in range(len(arr)):
        arr[i] = chr(arr[i] + 64)

    print("".join(arr))