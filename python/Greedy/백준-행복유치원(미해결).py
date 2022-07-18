N, K = map(int, input().split())
arr = list(map(int, input().split()))

group = [[] for _ in range(K)]

## 5 3
## 1 3 5 6 10
## 3개의 그룹이 필요
## len // 3 = 2
## if 5개의 그룹이 필요할때는?
## len // 5 = 1

cnt = 0
group_number = 0

for i in range(0, len(arr)):
    print(group)
    if cnt == 0:
        ## group_number에 해당하는 그룹이 비어있을 때
        group[group_number].append(arr[i])
        cnt += 1
    else:
        if i + 1 < len(arr) and arr[i] - arr[i - 1] <= arr[i + 1] - arr[i]:
            group[group_number].append(arr[i])
            cnt += 1
        else:
            group_number += 1
            if group_number >= K:
                group_number = K - 1
            group[group_number].append(arr[i])
            cnt = 0

    if len(arr) / K <= cnt:
        group_number += 1
        cnt = 0

    if group_number >= K:
        group_number = K - 1

answer = 0
for i in range(0, len(group)):
    if len(group[i]) > 1:
        answer += (max(group[i])- min(group[i]))

print(answer)