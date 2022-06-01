n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def s(arr1, arr2):
    result = 0
    for i in range(0, n):
        result += (arr1[i] * arr2[i])
    return result

## 배열 a를 오름차순 정렬
a.sort()

temp = list()

# for i in range(0, n):
    
            
print(s(a, b))


