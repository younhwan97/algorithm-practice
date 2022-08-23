import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    str = input().strip()

    reversed_str = str[::-1]

    if str == reversed_str:
        ## 그 자체로 회문
        print(0)
    else:
        ans = -1

        for i in range(len(str)):
            if str[i] != reversed_str[i]:
                temp = str[:i] + str[i+1:]
                temp2 = reversed_str[:i] + reversed_str[i+1:]
                
                if temp == temp[::-1] or temp2 == temp2[::-1]:
                    ans = 1
                else:
                    ans = 2

                break

        print(ans)