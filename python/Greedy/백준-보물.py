n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def s(arr1, arr2):
    result = 0
    for i in range(0, n):
        result += (arr1[i] * arr2[i])
    return result

print(s(a, b))


