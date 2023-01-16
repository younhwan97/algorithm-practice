import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

if sorted(arr) == arr and arr[0] == 1 and arr[-1] == 8:
    print("ascending")
elif sorted(arr, reverse = True) == arr and arr[0] == 8 and arr[-1] == 1:
    print("descending")
else:
    print("mixed")