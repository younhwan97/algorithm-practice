import sys
input = sys.stdin.readline







##### 
#   *
# *   *
#   * 
# 이러한 경우를 처리 불가
#
# N, M, L, K = map(int, input().split())
# position = list()
# for _ in range(K):
#     x, y = map(int, input().split())
#     position.append((x, y))

# def check(x1, y1, x2, y2, L, dir):
#     res = False

#     if dir == 0: # 좌층 상단
#         if (x1 - L <= x2 <= x1) and (y1 - L <= y2 <= y1):
#             res = True
#     elif dir == 1: # 우측 상단
#         if (x1 <= x2 <= x1 + L) and (y1 - L <= y2 <= y1):
#             res = True
#     elif dir == 2: # 좌측 하단
#         if (x1 - L <= x2 <= x1) and (y1 + L >= y2 >= y1):
#             res = True
#     elif dir == 3: # 우측 하단
#         if (x1 + L >= x2 >= x1) and (y1 + L >= y2 >= y1):
#             res = True
#     return res

# cnt = 0
# for x1, y1 in position:
#     tmp = 0
#     for dir in range(4):
#         tmp2 = 0
#         for x2, y2 in position:
#             if check(x1, y1, x2, y2, L, dir):
#                 tmp2 += 1
#         tmp = max(tmp, tmp2)
#     cnt = max(cnt, tmp)
# print(K - cnt)