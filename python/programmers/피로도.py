answer = -1

def search(now_k, fight, dungeons, min_k):
    global answer
    
    if len(fight) == len(dungeons) or now_k < min_k:
        answer = max(answer, len(fight))
        return
    
    for i in range(len(dungeons)):
        if i not in fight:
            if now_k >= dungeons[i][0]:
                fight.add(i)
                search(now_k - dungeons[i][1], fight, dungeons, min_k)
                fight.remove(i)


def solution(k, dungeons):
    global answer
    
    min_k = 1001
    
    for i in range(len(dungeons)):
        if min_k > dungeons[i][0]:
            min_k = dungeons[i][0]
 
    fight = set()
    search(k, fight, dungeons, min_k)    
    return answer