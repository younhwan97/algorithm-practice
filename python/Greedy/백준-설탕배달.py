n = int(input())

## 배달해야 하는 봉지의 최소 개수
answer = 0

while True:
    if n == 0:
        break
    else:
        if n % 5 == 0:
            answer += (n // 5)
            n = 0
        elif n < 3:
            answer = -1
            break    
        else:
            n -= 3    
            answer += 1

print(answer)