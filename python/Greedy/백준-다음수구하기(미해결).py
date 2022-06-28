T = int(input())

for _ in range(T):
    number = list(input())
    number = list(map(int, number))

    if number == sorted(number, reverse=True):
        print("BIGGEST")
    else:
        value = number.copy()

        for i in range(0, len(number)):
            temp = number[len(number) - 1 - i]

            for j in range(0, len(number)):
                temp_2 = number[len(number) - i - j - 1]

                if temp_2 < temp:
                    value[len(number) - i - j - 1] = temp
                    value[len(number) - i - 1] = temp_2
                    break
            
            




