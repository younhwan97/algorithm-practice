import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())
        parent = [-1] * (N + 1)

        for _ in range(N - 1):
            a, b = map(int, input().split())
            parent[b] = a
        
        A, B = map(int, input().split())
    
        q1 = []
        q2 = []

        q1.append(A)
        q2.append(B)

        while True:
            value = parent[A]

            if value == -1:
                break

            q1.append(value)
            A = value

        while True:
            value = parent[B]

            if value == -1:
                break

            q2.append(value)
            B = value
            
        ans = -1
        for a in q1:
            for b in q2:
                if a == b:
                    ans = a
                    break
            if ans != -1:
                break

        print(ans)

solve()