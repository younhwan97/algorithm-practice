import sys
input = sys.stdin.readline

g = int(input())
p = int(input())
arr = list()
gate = [0] * g

for _ in range(p):
    arr.append(int(input()))

for i in range(len(arr)):
    can_docking = False

    for j in range(arr[i] - 1, -1, -1):
        if gate[j] == 0:
            gate[j] = 1
            can_docking = True
            break
    
    if not can_docking:
        break

cnt = 0
for i in range(len(gate)):
    if gate[i] == 1:
        cnt += 1

print(cnt)