import sys
sys.setrecursionlimit(10 ** 6)
answer = 0
tmp = 0

def search(words, now, target):
    global answer, tmp
    
    if now == target:
        answer = tmp
    
    tmp += 1
    
    if len(now) == 5:
        return
    
    for i in range(len(words)):
        search(words, now + words[i], target)
    

def solution(word):
    global answer
    words = ["A", "E", "I", "O", "U"]
    search(words, "", word)
    return answer