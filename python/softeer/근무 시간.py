import sys
input = sys.stdin.readline

ans = 0

for _ in range(5):
    start, end = input().split()

    start_hour, start_minute = start.split(":")
    start_total = int(start_hour) * 60 + int(start_minute)

    end_hour, end_minute = end.split(":")
    end_total = int(end_hour) * 60 + int(end_minute)

    ans += (end_total - start_total)

print(ans)