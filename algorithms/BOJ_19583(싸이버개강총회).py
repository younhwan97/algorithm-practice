import sys
input = sys.stdin.readline

S, E, Q = input().split()

def hhmm_to_total(target):
    hh, mm = target.split(":")
    hh, mm = int(hh), int(mm)
    return hh * 60 + mm

dic = dict()
ans = 0
while True:
    info = input().rstrip()
    if not info: break
    hhmm, nickname = info.split()
    
    if hhmm_to_total(hhmm) <= hhmm_to_total(S):
        dic[nickname] = 1
    elif hhmm_to_total(E) <= hhmm_to_total(hhmm) <= hhmm_to_total(Q):
        if nickname in dic and dic[nickname] == 1:
            ans += 1
            dic[nickname] = 0
print(ans)