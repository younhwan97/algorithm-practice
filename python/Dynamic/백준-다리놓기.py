def com(n, r):
    return fac(n) //  (fac(n - r) * fac(r))
    
def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n -1)

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())

    print(com(m, n))    