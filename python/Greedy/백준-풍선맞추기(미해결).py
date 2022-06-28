N = int(input())
arr = list(map(int, input().split()))

h = arr[0]

answer = 0

finish_infinite_loop = False
hit_first_shot = False

for i in range(0, N):
    if arr[i] == 0:
        arr[i] = -1

while True:
    if finish_infinite_loop == True:
        break
    else:
        answer += 1

        for i in range(0, N):
            if arr[i] == h:
                hit_first_shot = True
                arr[i] = -1
                h -= 1
            elif hit_first_shot == True:
                h -= 1
            
            if h == 0:
                break
        
        check_finish_loop = True
        
        for i in range(0, N):
            if arr[i] != -1:
                h = arr[i]
                hit_first_shot = False
                check_finish_loop = False
                break
        
        if check_finish_loop == True:
            finish_infinite_loop = True

print(answer)