import sys

N = int(sys.stdin.readline())
arr_minus = list()
arr_zero = list()
arr_plis = list()

for _ in range(N):
    temp = int(sys.stdin.readline())

    if temp > 0:
        arr_plis.append(temp)
    elif temp < 0:
        arr_minus.append(temp)
    else:
        arr_zero.append(temp)

arr_minus.sort()
arr_plis.sort(reverse=True)

answer = 0

while arr_minus:
    if len(arr_minus) == 1:
        break
    else:
        temp = arr_minus[0] * arr_minus[1]
        answer += temp
        del arr_minus[0]
        del arr_minus[0]

while arr_zero:
    if len(arr_minus) == 0:
        break
    else:
        del arr_zero[0]
        del arr_minus[0]

while arr_plis:
    if len(arr_plis) == 1:
        break
    else:
        temp = arr_plis[0] * arr_plis[1]
        if temp > arr_plis[0] + arr_plis[1]:
            answer += temp
        else:
            answer += arr_plis[0] + arr_plis[1]
        del arr_plis[0]
        del arr_plis[0]
answer += (sum(arr_minus) + sum(arr_plis))
print(answer)