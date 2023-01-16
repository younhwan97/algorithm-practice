import sys
input = sys.stdin.readline

A, B = map(int, input().split())

if A > B:
    print('A')
elif B > A:
    print('B')
else:
    print("same")