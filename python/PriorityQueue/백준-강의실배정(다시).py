import sys
from queue import PriorityQueue

N = int(input())

lecture = list()
room = PriorityQueue()

for _ in range(N):
    s, t = map(int, sys.stdin.readline().split())

    lecture.append([s, t])

lecture.sort()

for i in range(0, len(lecture)):
    if room.qsize() == 0:
        room.put(lecture[i][1])
    else:
        t = room.get()

        if t > lecture[i][0]:
            room.put(t)

        room.put(lecture[i][1])

print(room.qsize())