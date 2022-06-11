import sys

N = int(input())
price_a, price_b = map(int, input().split())

a_kcal = int(input())
b_kcal = list()

for _ in range(N):
    b_kcal.append(int(sys.stdin.readline()))

b_kcal.sort(reverse=True)

kcal_sum = a_kcal
price = price_a

for i in range(0, len(b_kcal)):
    if kcal_sum // price <= (kcal_sum + b_kcal[i]) // (price + price_b):
        kcal_sum += b_kcal[i]
        price += price_b

print(kcal_sum // price)