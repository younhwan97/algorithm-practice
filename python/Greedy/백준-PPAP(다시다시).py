import sys

input = sys.stdin.readline

str = input().strip()

if len(str) == 1:
    if str == "P":
        print("PPAP")
    else:
        print("NP")
elif 1 < len(str) < 4:
    print("NP")
elif len(str) == 4:
    if str == "PPAP":
        print("PPAP")
    else:
        print("NP")
else:
    p_cnt = 0
    is_success = True
    for i in range(len(str)):
        if str[i] == 'P':
            p_cnt += 1
        elif str[i] == 'A':
            if p_cnt >= 2 and i + 1 < len(str) and str[i + 1] == 'P':
                p_cnt -= 2
            else:
                is_success = False
                break

    if is_success:
        print("PPAP")
    else:
        print("NP")