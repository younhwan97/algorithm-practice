import sys
input = sys.stdin.readline

## 큐로 풀어볼 것 !!

def get_cnt(belt):
    cnt = 0
    for i in range(len(belt)):
        if belt[i][0] <= 0:
            cnt += 1
    return cnt

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    belt = []
    
    for i in range(len(arr)):
        belt.append([arr[i], 0]) # 내구도, 로봇의 개수
    
    lev = 0
    while True:
        lev += 1

        # 내리는 위치 확인
        if belt[n - 1][1] == 1:
            belt[n - 1][1] = 0

        # 회전
        new_belt = []
        new_belt.append(belt[-1])
        for i in range(len(belt) - 1):
            new_belt.append(belt[i])

        # 로봇 이동
        if new_belt[n - 1][1] == 1:
            new_belt[n - 1][1] = 0
            
        for i in range(n - 2, -1, -1):
            if new_belt[i][1] == 1 and new_belt[i + 1][1] == 0 and new_belt[i + 1][0] >= 1:
                new_belt[i + 1][1] = 1
                new_belt[i + 1][0] -= 1
                new_belt[i][1] = 0
        
        # 올리는 위치 확인
        if new_belt[0][0] >= 1:
            new_belt[0][1] = 1
            new_belt[0][0] -= 1

        # 내구도 확인
        cnt = get_cnt(new_belt)

        if cnt >= k:
            break
        else:
            belt = new_belt
        
    print(lev)

solve()