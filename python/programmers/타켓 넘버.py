def search(index, value, numbers, target):
    if index == len(numbers):
        if value == target:
            return 1
        return 0
    
    ans = 0

    # +
    ans += search(index + 1, value + numbers[index], numbers, target)
    # -
    ans += search(index + 1, value - numbers[index], numbers, target)
    
    return ans
    
def solution(numbers, target):
    answer = search(0, 0, numbers, target)
    return answer