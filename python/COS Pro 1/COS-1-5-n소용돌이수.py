#You may use import as below.
#import math

# def solution(n):
#     # Write code here.
#     a = [[0] * n for _ in range(n)]
#     ## 만약 삼각형이라면?
#     ## a = [[0] * i for i in range(n)]
    
#     dir = 0 # 방향
#     loop = n
#     r, c = 0, -1 # 좌표의 초기값
#     dr = [0, 1, 0, -1]
#     dc = [1, 0, -1, 0]
#     num = 0
    
#     while num < n * n:
#         for _ in range(loop):
#             r = r + dr[dir]
#             c = c + dc[dir]
#             num += 1
#             a[r][c] = num
        
#         dir = (dir + 1) % 4
#         if dir % 2 == 1:
#             loop -= 1

#     answer = 0
#     for i in range(n):
#         answer += a[i][i]

#     return answer

def solution(n):
    answer = 1
    now = 1

    n -= 1
    while n > 0:
        now += 2 * n
        answer += now

        if n == 1:
            break
        
        now += 2 * n
        answer += now
        n -= 2

    return answer
    
#The following is code to output testcase.
n1 = 5
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")