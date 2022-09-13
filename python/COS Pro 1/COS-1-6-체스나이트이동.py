#You may use import as below.
#import math

def solution(pos):
    # Write code here.
    answer = 0
    
    x = ord(pos[0]) - ord('A')
    y = ord(pos[1]) - ord('1')

    dx = [-2, -2, -1, -1, 2, 1, 2, 1]
    dy = [1, -1, 2, -2, 1, 2, -1, -2]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < 8) and (0 <= ny < 8):
            answer += 1

    return answer

#The following is code to output testcase.
pos = "A7"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")