n = int(input())

answer = 0

sum = 0
count = 1

while sum <= n:
    sum += count
    answer += 1
    count = count + 1

print(answer - 1)