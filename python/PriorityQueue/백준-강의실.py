import sys
from queue import PriorityQueue

N = int(input())

lecture = []
room = PriorityQueue()

for _ in range(N):
    n, s, e = map(int, sys.stdin.readline().split())

    lecture.append((s, e))

lecture.sort()

for i in range(N):
    if room.qsize() == 0:
        room.put(lecture[i][1])
    else:
        temp = room.get()

        if lecture[i][0] < temp:
            room.put(temp)
   
        room.put(lecture[i][1])

print(room.qsize())