import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = []
for _ in range(N):
    arr.append(input().rstrip())

# 탐색
word1, word2, ans = "", "", 0
for i in range(N):
    # 검사할 문자의 길이가 ans보다 작을 경우
    # 검사를 할 필요가 없음(최대로 길어봤자 ans보다 작기 때문에)
    if len(arr[i]) < ans: continue

    for j in range(i + 1, N):
        # 최대 길이
        length = min(len(arr[i]), len(arr[j]))
        if length < ans or arr[i] == arr[j]: continue

        cnt = 0
        for k in range(length):
            if arr[i][k] == arr[j][k]:
                cnt += 1
            else:
                break
        if cnt > ans:
            word1, word2, ans = arr[i], arr[j], cnt

print(word1)
print(word2)