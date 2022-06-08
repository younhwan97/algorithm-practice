str = input().split()
ucpc = ['U', 'C', 'P', 'C']

ucpc_index = 0
answer = ""

for index in range(0, len(str)):
    if str[index].find('UCPC'):
        answer = 'UCPC'
        break

    if ucpc_index < len(ucpc):
        if str[index][0] == ucpc[ucpc_index]:
            answer += ucpc[ucpc_index]
            ucpc_index += 1
    else:
        break

if answer == 'UCPC':
    print("I love UCPC")
else:

    print("I hate UCPC")