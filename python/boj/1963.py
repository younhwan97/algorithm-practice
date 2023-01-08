import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b, distance, primes):
    distance[a] = 0

    que = deque()
    que.append(a)

    while que:
        value = que.popleft()

        if value == b:
            break

        arr = list(str(value))

        for i in range(len(arr)):
            for j in range(0, 10):
                origin = arr[i]
                arr[i] = str(j)

                new_value = int("".join(arr))

                if (1000 <= new_value <= 9999) and new_value in primes:
                    if distance[new_value] == -1:
                        distance[new_value] = distance[value] + 1
                        que.append(new_value)
                    else:
                        if distance[new_value] > distance[value] + 1:
                            distance[new_value] = distance[value] + 1
                            que.append(new_value)
                            
                arr[i] = origin
                
def solve():
    T = int(input())

    # 소수 구하기
    arr = [True] * (10000)
    primes = set()

    for i in range(2, 10000):
        if arr[i]:
            primes.add(i)

            for j in range(2 * i, 10000, i):
                arr[j] = False
    
    # 풀이
    for _ in range(T):
        a, b = map(int, input().split())
        distance = [-1] * 10000
      
        bfs(a, b, distance, primes)

        print(distance[b])

solve()