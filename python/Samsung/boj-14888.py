import sys
input = sys.stdin.readline

max_value = -1 * 1_000_000_000_000
min_value = 1_000_000_000_000

def operation(arr, oper_cnt, value, index):
    global max_value
    global min_value

    if index == len(arr):
        max_value = max(value, max_value)
        min_value = min(value, min_value)

    for i in range(len(oper_cnt)):
        if oper_cnt[i] != 0:
            oper_cnt[i] -= 1
            if i == 0:
                new_value = value + arr[index]
            elif i == 1:
                new_value = value - arr[index]
            elif i == 2:
                new_value = value * arr[index]
            else:
                if value < 0:
                    new_value = (-1 * value) // arr[index]
                    new_value *= -1
                else:
                    new_value = value // arr[index]

            operation(arr, oper_cnt, new_value, index + 1)
            oper_cnt[i] += 1

def solve():
    # 입력
    n = input()
    arr = list(map(int, input().split()))
    oper_cnt = list(map(int, input().split()))

    # 브루트 포스
    operation(arr, oper_cnt, arr[0], 1)

    # 결과 출력
    answer = (max_value, min_value)
    return answer

res = solve()

print(res[0])
print(res[1])