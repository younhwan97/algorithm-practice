import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        a = int(input())
        arr.append(a)

    arr.sort()

    count = min(m, n)
    sale = arr[0] * count
    price = arr[0]

    for i in range(1, len(arr)):
        tmp = m - i
        count = min(tmp, n)

        if sale < arr[i] * count:
            sale = arr[i] * count
            price = arr[i]

    print(price, sale)

solve()