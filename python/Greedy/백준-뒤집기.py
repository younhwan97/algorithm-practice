n = list(input())

group_0 = 0
group_1 = 0

for index in range(0, len(n)):
    if index + 1 < len(n) and n[index] != n[index + 1]:
        if n[index] == '0':
            group_0 += 1
        else:
            group_1 += 1    
    elif index + 1 == len(n):
        if n[index] == '0':
            group_0 += 1
        else:
            group_1 += 1           

if group_1 == 0 or group_0 == 0:
    print(0)
else:
    if group_0 < group_1:
        print(group_0)
    else:
        print(group_1)