def func_a(n):
    ret = 1 # 1 -> 10 -> 100 ..
    while n > 0:
        ret *= 10
        n -= 1
    return ret

## n = 367 -> 36 -> 3 -> 0
## ret = 0 -> 1 -> 2 -> 3(자릿수)
def func_b(n):
    ret = 0 # 1 -> 2 -> 3 -> 4 ..
    while n > 0:
        ret += 1
        n //= 10
    return ret

## n = 367 -> 36 -> 3 -> 0
## ret = 0 -> 7 -> 13 -> 16(각 자릿수의 합)
def func_c(n):
    ret = 0
    while n > 0:
        ret += n%10
        n //= 10
    return ret

def solution(num):
    next_num = num
    while True:
        next_num += 1
        length = func_b(next_num)
        if length % 2:
            continue
        
        divisor = func_a(length // 2)  
        front = next_num // divisor
        back = next_num % divisor
        
        front_sum = func_c(front)
        back_sum = func_c(back)
        
        if front_sum == back_sum:
            break
            
    return next_num

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
num1 = 1
ret1 = solution(num1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

num2 = 235386
ret2 = solution(num2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")