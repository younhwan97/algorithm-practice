n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = 0

for i in range(0, n):
    a.remove(min(a))
    b.remove(max(b))
    answer += (min(a) * max(b))

print(answer)