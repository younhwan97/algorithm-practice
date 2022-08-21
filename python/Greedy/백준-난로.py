import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list()

for _ in range(n):
    arr.append(int(input()))

if k >= n:
    ## 성냥의 개수가 충분할 때
    ### 손님이 올 때 마다 난로를 켬
    print(n)
elif k == 1:
    ## 성냥의 개수가 1개일 때
    print(max(arr))
else:
    dif = list()

    for i in range(len(arr)):
        if i + 1 < len(arr):
            dif.append(arr[i + 1] - arr[i])
    
    dif.sort(reverse=True)
    dif = dif[k - 1:]
    
    for _ in range(k):
        dif.append(1)
   
    print(sum(dif))