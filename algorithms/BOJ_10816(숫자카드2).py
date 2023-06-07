import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

dic = dict()
for card in cards:
    if card in dic:
        dic[card] += 1
    else:
        dic[card] = 1

for target in targets:
    if target in dic:
        print(dic[target], end = " ")
    else:
        print(0, end = " ")