def get_dif_cnt(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt

def dfs(now, target, words, used, cnt):
    if now == target:
        return cnt
    
    ans = 1000
    for i in range(len(words)):
        if get_dif_cnt(now, words[i]) == 1 and not used[i]:
            new_used = used.copy()
            new_used[i] = True
            ans = min(ans, dfs(words[i], target, words, new_used, cnt + 1))
    
    return ans

def solution(begin, target, words):
    answer = 0
    
    if target in words:
        used = [False] * len(words)
        answer = dfs(begin, target, words, used, 0)
            
    return answer