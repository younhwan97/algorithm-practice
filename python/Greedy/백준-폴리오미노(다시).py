str = list(input())

for index in range(0, len(str)):
    if str[index] == 'X':
        pass_validation_check = True

        if index + len('AAAA') <= len(str):
            for j in range(1, 4):
                if str[index + j] != 'X':
                    pass_validation_check = False

            if pass_validation_check == True:
                for j in range(0, 4):
                    str[index + j] = 'A'
            else:
                if str[index + 1] == 'X':
                    str[index] = 'B'
                    str[index + 1] = 'B'
        elif index + len('BB') <= len(str):
            if str[index + 1] == 'X':
                    str[index] = 'B'
                    str[index + 1] = 'B'

answer = ""

for word in str:
    if word != 'X':
        answer += word
    else:
        answer = -1
        break

print(answer)

## replace를 이용해 훨씬 쉽게 해결 가능