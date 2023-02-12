import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

ans = -1

for i in range(N):
    x1, y1 = i, arr[i]

    cnt = 0
    for j in range(N):
        if i != j:
            x2, y2 = j, arr[j]
            a = (y2 - y1) / (x2- x1) # 기울기
            b = y1 - a * x1 # y = kx + b

            flag = True
            if i > j:
                for k in range(j + 1, i):
                    height = a * k + b
                    if height <= arr[k]:
                        flag = False
                        break
            elif j > i:
                for k in range(i + 1, j):
                    height = a * k + b
                    if height <= arr[k]:
                        flag = False
                        break
            
            if flag:
                cnt += 1
    ans = max(cnt, ans)
print(ans)