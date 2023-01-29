import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    target = list(input().strip())
    K = int(input())
    N = int(len(target))

    alph_cnt = [0] * 26

    for alph in target:
        alph_cnt[ord(alph) - 97] += 1
    
    for i in range(N):
        
