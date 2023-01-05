import sys
input = sys.stdin.readline

def solve():
    T = int(input())

    cnt = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    for _ in range(T):
        N = int(input())

        max_value = -1
        min_value = -1

        if N < 5:
            # 만들 수 있는 자릿수 -> 1
            ## max
            for i in range(9, -1, -1):
                if cnt[i] == N:
                    max_value = i
                    break
            ## min
            for i in range(0, 10):
                if cnt[i] == N:
                    min_value = i
                    break
        else:
            ## max
            tmp = ['1'] * (N // 2)

            if N % 2 != 0:
                tmp[0] = '7'
            
            max_value = int("".join(tmp))

            ## min
            if N <= 7:
                for i in range(1, 10):
                    if cnt[i] == N:
                        min_value = i   
                        break
            else:
                tmp = [-1] * (N // 7 + 1)

                for i in range(len(tmp) - 1, -1, -1):
                    if i != 0:
                        if N - 7 >= 2:
                            tmp[i] = '8'
                            N -= 7
                        else:
                            tmp[i] = '0'
                            N -= 6
                    else:
                        for j in range(1, 10):
                            if cnt[j] == N:
                                tmp[0] = str(j)

                min_value = int("".join(tmp))

        print(min_value, max_value)

solve()