import sys

input = sys.stdin.readline

N, K = map(int, input().split())

if K * (K + 1) // 2 > N:
    print(-1)
elif K * (K + 1) // 2 == N:
    print(K - 1)
else:
    if (N - K * (K + 1) // 2) % K == 0:
        print(K - 1)
    else:
        print(K) 