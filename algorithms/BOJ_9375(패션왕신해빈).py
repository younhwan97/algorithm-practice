import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    dic = dict()
    for _ in range(N):
        name, cloth_type = input().split()
        if cloth_type in dic:
            dic[cloth_type] += 1
        else:
            dic[cloth_type] = 1

    ans = 1
    for t in dic:
        ans *= (dic[t] + 1)

    print(ans - 1)