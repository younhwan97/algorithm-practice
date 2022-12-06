import sys
input = sys.stdin.readline

def solve():
    target = input().strip()

    ans = "PPAP"
    if len(target) > 4:
        p_cnt = 0

        for i in range(len(target)):
            if target[i] == 'P':
                p_cnt += 1
            elif target[i] == 'A':
                if p_cnt >= 2 and i + 1 < len(target) and target[i + 1] == 'P':
                    p_cnt -= 2
                else:
                    ans = "NP"
                    break
    elif len(target) == 4:
        if target != 'PPAP':
            ans = 'NP'
    elif  1 < len(target) < 4:
        ans = 'NP'
    elif len(target) == 1:
        if target != 'P':
            ans = "NP"

    print(ans)

solve()