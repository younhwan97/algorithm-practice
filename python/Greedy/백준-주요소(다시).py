N = int(input())
length = list(map(int, input().split())) 
price = list(map(int, input().split()))
del price[len(price) - 1]

arr = []

for i in range(N - 1):
    temp = length[i:]
    temp_sum = sum(temp)
    arr.append((price[i], temp_sum))

arr.sort()
length_sum = sum(length)
price_sum = 0
print(arr)
for i in range(len(arr)):
    temp = arr[i]
    price = temp[0]
    length = temp[1]

    length_sum -= length

    if length_sum >= 0:
        price_sum += (price * length)
    else:
        length_sum += length
        price_sum += (price * length_sum)
        break