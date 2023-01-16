import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())

secret = input().strip()
code = input().strip()

if len(code) >= len(secret) and secret in code:
    print("secret")
else:
    print("normal")