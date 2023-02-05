import sys
input = sys.stdin.readline

number = list(map(int, input().strip()))
now = number[0]
last = number[0]

index = 0
while index + 1 < len(number):
    if number[index + 1] > last:
        # 같은 자리 수
        gap = number[index + 1] - last
        now += gap
        last = number[index + 1]
        index += 1
    else:
        next = now # 다음 타겟 수
        while True:
            next += 1

            if str(number[index + 1]) in str(next):
                now = next
                last = number[index + 1]
                index += 1
                break
        
        tmp = ""
        index2 = index
        while len(tmp) < len(str(next)) and index2 < len(number):
            if tmp + str(number[index2]) not in str(next):
                break
            else:
                tmp += str(number[index2])
                index2 += 1
        
        if len(tmp) > 1:
            index = index + len(tmp) - 1

        
print(now)
