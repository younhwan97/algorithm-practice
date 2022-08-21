import sys
input = sys.stdin.readline

n = int(input())

start_m = 0
start_d = 0
end_m = 0
end_d = 0

cnt = 0
for _ in range(n):
    s_m, s_d, e_m, e_d = map(int, input().split())

    if start_m == 0:
        start_m = s_m
        start_d = s_d
        end_m = e_m
        end_d = e_d
        cnt += 1
    else:
        if (s_m == 3 and s_d <= 1) or (s_m < 3):
            if end_m < e_m or (end_m == e_m and end_d < e_d):
                start_d = s_d
                start_m = s_m
                end_m = e_m
                end_d = e_d
        else:
            if (s_m == end_m and s_d < end_d) or (s_m < end_m):
                if end_m < e_m or (end_m == e_m and end_d < e_d):
                    end_m = e_m
                    end_d = e_d

print(cnt)
            