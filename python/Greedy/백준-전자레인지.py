n = int(input())

answer_300 = 0
answer_60 = 0
answer_10 = 0
answer = 0

while True:
    if n == 0:
        ##
        break
    else:
        if n >= 300:
            n -= 300
            answer_300 += 1
        elif n >= 60:
            n -= 60
            answer_60 += 1
        elif n >= 10:
            n -= 10
            answer_10 += 1 
        else:
            answer = -1
            break    

if answer == -1:
    print(answer)
else:
    print(str(answer_300) + " " + str(answer_60) + " " + str(answer_10))