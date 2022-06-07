N, M = map(int, input().split())
price = list()
answer = 0

for _ in range(M):
    bundle, individually = map(int, input().split())
    price.append([bundle, individually])

## 패키지 가격이 낮은 순으로 정렬
price.sort()

while True:
    if N >= 6:
        price.sort()
        temp_price_1 = price[0][0]

        price.sort(key=lambda x:x[1])

        temp_price_2 = price[0][1] * 6

        if temp_price_1 > temp_price_2:
            answer += temp_price_2
        else:
            answer += temp_price_1
        N -= 6
    elif N == 0:
        break
    else:
        price.sort()
        if price[0][0] > N * price[0][1]:
            temp_price_1 = N * price[0][1]
        else:
            temp_price_1 = price[0][0]

        price.sort(key=lambda x:x[1])

        if price[0][0] > N * price[0][1]:
            temp_price_2 = N * price[0][1]
        else:
            temp_price_2 = price[0][0]

        if temp_price_1 > temp_price_2:
            answer += temp_price_2
        else:
            answer += temp_price_1
        N = 0

print(answer)