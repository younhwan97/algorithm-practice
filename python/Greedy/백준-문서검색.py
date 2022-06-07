document = input()
keyword = input()

answer = 0 

while True:
    index = document.find(keyword)
    if index == -1:
        break
    else:
        answer += 1
        if index == 0:
            document = document[len(keyword):]
        else:
            document = document[index + len(keyword):]
print(answer)