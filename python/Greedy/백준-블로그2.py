n = int(input())
arr = list(input())

B_count = 0
R_count = 0

for i in range(0, len(arr)):
    if i + 1 < len(arr):
        if arr[i] != arr[i + 1]:
            if arr[i] == 'B':
                B_count += 1
            else:
                R_count += 1    
    else:
        if arr[i] == 'B':
            B_count += 1
        else:
            R_count += 1

answer = 0

if R_count < B_count:
    answer = R_count + 1
else:
    answer = B_count + 1

print(answer)