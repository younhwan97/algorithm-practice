import sys
input = sys.stdin.readline

n = int(input())

man = list(map(int, input().split()))
women = list(map(int, input().split()))

plus_man = list()
minus_man = list()
plus_women = list()
minus_women = list()

for i in range(n):
    if man[i] > 0:
        plus_man.append(man[i])
    else:
        minus_man.append(man[i])

    if women[i] > 0:
        plus_women.append(women[i])
    else:
        minus_women.append(women[i])

cnt = 0

## 마이너스 남자, 플러스 여자
minus_man.sort()
plus_women.sort(reverse=True)
index = 0
for i in range(len(minus_man)):
    for j in range(index, len(plus_women)):
        if -1 * minus_man[i] > plus_women[j]:
            cnt += 1
            index = j + 1
            break
        
        if j == len(plus_women) - 1:
            break

## 플러스 남자, 마이너스 여자
plus_man.sort(reverse=True)
minus_women.sort()
index = 0 
for i in range(len(plus_man)):
    for j in range(index, len(minus_women)):
        if plus_man[i] < -1 * minus_women[j]:
            cnt += 1
            index = j + 1
            break
        
        if j == len(minus_women) - 1:
            break
print(cnt)