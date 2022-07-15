A, B = map(int, input().split())
cnt = 1
while B > A:
    temp = list(str(B))
    last = temp[len(temp) - 1]

    if last == '1':
        temp = temp[:len(temp) - 1]
        value = ''
        for i in range(0, len(temp)):
            value += temp[i]
        value = int(value)
        B = value
    else:
        if B % 2 == 0:
            B = B // 2
        else:
            break
    
    cnt += 1

if A == B:
    print(cnt)
else:
    print(-1)