import sys

## 입력
input = sys.stdin.readline

L, R = map(int, input().split())

if len(str(L)) != len(str(R)):
    print(0)
else:
    arr_1 = str(L)
    arr_2 = str(R)

    flag = False
    cnt = 0
    for i in range(0, len(arr_1)):
        if arr_1[i] != arr_2[i]:
            flag = True
        
        if flag:
            continue

        if arr_1[i] == arr_2[i] and arr_1[i] == '8':
            cnt += 1

    print(cnt)