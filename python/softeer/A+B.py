import sys
input = sys.stdin.readline

T = int(input())

for case in range(T):
    A, B = map(int, input().split())

    print("Case #" + str(case + 1) + ": " + str(A + B))