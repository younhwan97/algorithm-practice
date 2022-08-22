import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

can_hit = [1] * n
cnt = 0
for i in range(n):
    if can_hit[i] == 1:
        can_hit[i] = 0