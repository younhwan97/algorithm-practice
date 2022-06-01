exp = input().split("-")
result = 0

for index, value in enumerate(exp):
    temp = list(map(int, value.split("+")))
    for item in temp:
        if index == 0:
            result += item
        else:
            result -= item

print(result)