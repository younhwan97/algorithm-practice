import sys

n = int(input())

arr = list()
arr2 = list()
value = {}

for _ in range(n):
    s = input()
    temp = list(s)

    for i in range(0, len(temp)):
        value[temp[i]] = 0

    arr.append((len(temp), s))
    arr2.append(s)

arr.sort(reverse=True)
number = 9
while arr:
    temp = arr[0]

    length = temp[0]
    s = list(temp[1])[0]
     
    if value[s] == 0:
        value[s] = number
        number -= 1

    if length - 1 != 0:
        arr[0] = (length -1, temp[1][1:])
        arr.sort(reverse=True)
    else:
        del arr[0]

sum = 0
for i in range(0, len(arr2)):
    temp = ''

    for j in range(0, len(arr2[i])):
        temp += str(value[arr2[i][j]])

    sum += int(temp)

print(sum)