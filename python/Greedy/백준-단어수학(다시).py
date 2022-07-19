import sys

n = int(input())

arr = []
weight_arr = {}

for i in range(n):
    temp = list(input())
    arr.append(temp)
    for j in range(0, len(temp)):
        if temp[j] in weight_arr:
            weight_arr[temp[j]] += 10 ** (len(temp) - j - 1)
        else:
            weight_arr[temp[j]] = 10 ** (len(temp) - j - 1)

sorted_dict = sorted(weight_arr.items())
sorted_dict.sort(key = lambda x:x[1], reverse=True)

num = 9
for i in range(0, len(sorted_dict)):
    word = sorted_dict[i][0]

    weight_arr[word] = num
    num -= 1

sum = 0
for i in range(0, len(arr)):
    temp = ''
    for j in range(0, len(arr[i])):
        temp += str(weight_arr[arr[i][j]])
    
    sum += int(temp)
print(sum)