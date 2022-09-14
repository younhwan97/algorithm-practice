INC = 0
DEC = 1

def func_a(arr):
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = 1
    for i in range(1, length):
        if arr[i] != arr[i-1]:
            ret[i] = ret[i-1] + 1
        else:
            ret[i] = 2
    return ret

def func_b(arr):
    global INC, DEC
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = -1
    for i in range(1, length):
        if arr[i] > arr[i-1]:
            ret[i] = INC
        elif arr[i] < arr[i-1]:
            ret[i] = DEC
    return ret

def func_c(arr):
    ret = max(arr)
    if ret == 2:
        return 0
    return ret

def solution(S):
    check = func_@@@(@@@)
    dp = func_@@@(@@@)
    answer = func_@@@(@@@)
    return answer


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
S1 = [2, 5, 7, 3, 4, 6, 1, 8, 9]
ret1 = solution(S1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

S2 = [4, 3, 2, 1, 10, 6, 9, 7, 8]
ret2 = solution(S2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

S3 = [1, 2, 3, 4, 5]
ret3 = solution(S3)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")