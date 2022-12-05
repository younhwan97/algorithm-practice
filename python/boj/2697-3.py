import sys
input = sys.stdin.readline

# 규칙찾기로 해결함

def solve():
    T = int(input())

    for _ in range(T):
        nums = list(input().strip())

        # 숫자를 뒤에서 부터 확인하며 처음으로 수가 작아지는 부분을 찾는다.
        ## 279134399742의 경우 9 -> 3에서 처음으로 수가 작아진다.
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                break

        if index == -1:
            # 해당 구성으로 만들 수 있는 가장 큰 수
            print("BIGGEST")
        else:
            # 위에서 찾은 인덱스의 오른쪽에 위치한 수 가운데
            ## 위에서 찾은 인덱스의 값보다는 크며, 가장 작은 값을 찾는다.
            min_value_index = -1
            min_value = -1
            
            for i in range(index + 1, len(nums)):
                if nums[i] > nums[index]:
                    if min_value_index == -1:
                        min_value_index = i
                        min_value = nums[i]
                    else:
                        if min_value > nums[i]:
                            min_value = nums[i]
                            min_value_index = i
            
            # 값 교체
            tmp = nums[min_value_index]
            nums[min_value_index] = nums[index]
            nums[index] = tmp

            # 인덱스 이후로 정렬
            sorted_arr = list(map(int, nums[index + 1:]))
            sorted_arr.sort()
            
            # 정렬된 결과를 다시 리스트 마지막에 붙여주기
            new_arr = nums[:index + 1] + list(map(str, sorted_arr))

            # 결과 출력
            answer = "".join(new_arr)
            print(answer)
solve() 