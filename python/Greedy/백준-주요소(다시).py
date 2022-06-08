N = int(input())
length = list(map(int, input().split())) 
price = list(map(int, input().split()))

price_length_mapping = list()

for i in range(0, len(price) - 1):
    price_length_mapping.append([price[i], length[i]])

total_price = 0

for i in range(0, len(price_length_mapping)):
    min_price = price_length_mapping[i][0]
    for j in range(0, i):
        if min_price > price_length_mapping[j][0]:
            min_price = price_length_mapping[j][0]
    total_price += (min_price * price_length_mapping[i][1])

print(total_price)