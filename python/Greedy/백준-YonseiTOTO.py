import sys

N, M = map(int, input().split())
R = list()

for _ in range(N):
    required_m = 0

    ## n : 신청한 사람의 수
    ## k : 과목 수강 인원
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    ## 투자한 마일리지를 내림차순 정렬
    arr.sort(reverse=True)

    ## 과목을 신청하기 위한 최소 투자 마일리지를 구한다.
    if len(arr) < k:
        required_m = 1
    else:
        required_m = arr[k - 1]
    R.append(required_m)

R.sort()

sum = 0
answer = 0
for index in range(0, len(R)):
    if sum + R[index] <= M:
        sum += R[index]
        answer+=1
    else:
        break

print(answer)