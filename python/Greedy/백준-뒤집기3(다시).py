import sys
input = sys.stdin.readline

str = input().strip()

for i in range(1, len(str)):
    if str[i] < str[i - 1] and str[i] <= str[0]:
        temp = str[:i]
        temp = temp[::-1]
        str = temp + str[i:]

        temp = str[:i+1]
        temp = temp[::-1]
        str = temp + str[i+1:]

print(str)