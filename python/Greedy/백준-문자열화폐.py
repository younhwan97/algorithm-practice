import sys
input = sys.stdin.readline

n, x = map(int, input().split())

arr = [1] * n
total = 6

for i in range(len(arr)):
    for j in range(1, 27):
        temp = arr[len(arr) - 1 - i]
        total -= temp
        total += (27 - j)
        arr[len(arr) - 1 - i] = 27 - j
    
        if total <= x:
            break
    if total == x:
        break

if x < n or n * 26 < x:
    print("!")
else:
    str = ""

    for i in range(len(arr)):
        str += chr(arr[i] + 64)

    print(str)