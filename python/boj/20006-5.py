import sys
input = sys.stdin.readline

P, M = map(int, input().split())
rooms =[]
arr = []
for _ in range(P):
    lev, id = input().split()
    lev = int(lev)
    arr.append((id, lev))

rooms.append([arr[0]])

for i in range(1, P):
    flag = False
    for j in range(len(rooms)):
        if len(rooms[j]) < M:
            if abs(arr[i][1] - rooms[j][0][1]) <= 10:
                rooms[j].append(arr[i])
                flag = True
                break
    
    if not flag:
        rooms.append([arr[i]])
    
for room in rooms:
    if len(room) == M:
        print("Started!")
    else:
        print("Waiting!")
    
    room.sort()
    
    for id, lev in room:
        print(lev, id)