import sys
input = sys.stdin.readline

answer = -1

def find(arr, now, result):
    global answer

    # 종료 조건
    if now == len(arr):
        answer = max(answer, result)
        return

    # 현재 날짜에 일을 할 경우
    if now + arr[now][0] <= len(arr):
        find(arr, now + arr[now][0], result + arr[now][1])

    # 현재 날짜에 일을 하지 않을 경우
    find(arr, now + 1, result)
        

def solve():
    # 입력
    n = int(input())
    arr = list()

    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))

    # 브루트 포스
    find(arr, 0, 0)

    # 출력
    print(answer)
 
solve()