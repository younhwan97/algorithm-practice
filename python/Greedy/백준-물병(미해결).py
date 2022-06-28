N, K = map(int, input().split())
arr = [1] * N

answer = 0

while True:
    if len(arr) <= K:
        break
    