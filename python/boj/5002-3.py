import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = list(input().strip())

    m_cnt = 0
    w_cnt = 0

    for i in range(len(s)):
        if abs(m_cnt - w_cnt) == n and i + 1 < len(s):
            finish_loop = True
            if m_cnt > w_cnt:
                for j in range(i, i + 2):
                    if s[j] == 'W':
                        w_cnt += 1

                        tmp = s[i]
                        s[i] = s[j]
                        s[j] = tmp
                        finish_loop = False
                        break
            else:
                for j in range(i, i + 2):
                    if s[j] == 'M':
                        m_cnt += 1

                        tmp = s[i]
                        s[i] = s[j]
                        s[j] = tmp
                        finish_loop = False
                        break
            if finish_loop:
                break
        elif (m_cnt == 0 and w_cnt == 0) or (0 <= abs(m_cnt - w_cnt) < n):
            if s[i] == 'W':
                w_cnt += 1
            else:
                m_cnt += 1
        else:
            break

    print(m_cnt + w_cnt)

solve()