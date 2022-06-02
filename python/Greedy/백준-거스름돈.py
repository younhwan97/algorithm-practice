change = 1000 - int(input())
arr = [500, 100, 50, 10, 5, 1]

answer = 0

for item in arr:
    if change // item != 0:
        answer += change // item
        change = change % item
        
print(answer)