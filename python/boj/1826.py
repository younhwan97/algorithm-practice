import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list()

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a,b))

    distance, mount = map(int, input().split())
    arr.append((distance, 0))

    arr.sort()
    
    ans = 0
    
    for i in range(len(arr)):
        if arr[i][0] == distance:
            break

        if i == 0:
            d, m = arr[i]
        else:
            d = arr[i][0] - arr[i - 1][0]
            m = arr[i][1]
        mount -= d

        if mount < 0:
            ans = -1
            break

        tmp = 0
        for j in range(i + 1, len(arr)): tmp += arr[j][1]

        if distance - arr[i][0] > tmp + mount:
            mount += m
            ans += 1
        else:
            start = i
            last = i
            for j in range(i + 1, len(arr)):
                dif = arr[j][0] - arr[i][0]

                if dif > mount:
                    last = j
                    break

            if start != last:
                max_mount = -1

                for j in range(start, last):
                    max_mount = max(max_mount, arr[j][1])

                if max_mount == m:
                    mount += max_mount
                    ans += 1

    if mount < 0:
        print(-1)
    else:
        print(ans)

solve()