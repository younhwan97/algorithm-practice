import sys, heapq

A, B, N = map(int, sys.stdin.readline().split())

task = []
pq = []

for _ in range(N):
    time, color, count = sys.stdin.readline().split()

    time = int(time)
    count = int(count)

    heapq.heappush(task, (time, color, count))

while len(task) > 0:
    sub_task = heapq.heappop(task)

    sub_task_time = sub_task[0]
    sub_task_color = sub_task[1]
    sub_task_count = sub_task[2]

    for j in range(sub_task_count):
        if sub_task_color == 'B':
            heapq.heappush(pq, ((sub_task_time + j * A), sub_task_color))
        else:
            heapq.heappush(pq, ((sub_task_time + j * B), sub_task_color))
    
s_taks = []
j_task = []

number = 1

while len(pq) > 0:
    sub_task = heapq.heappop(pq)

    if sub_task[1] == 'B':
        s_taks.append(number)
    else:
        j_task.append(number)

    number += 1

print(len(s_taks))
for item in s_taks:
    print(item, end=" ")

print(len(j_task))
for item in j_task:
    print(item, end=" ")