answer = 0

def search(index, numbers, value, target):
    global answer
    
    if index == len(numbers):
        if value == target:
            answer += 1
        return

    n1 = value + numbers[index]
    search(index + 1, numbers, n1, target)

    n2 = value - numbers[index]
    search(index + 1, numbers, n2, target)

def solution(numbers, target):
    global answer

    search(0, numbers, 0, target)
    
    return answer