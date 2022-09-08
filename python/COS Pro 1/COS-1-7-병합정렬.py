def solution(N, votes):
    vote_counter = [0 for i in range(N+1)]
    for i in votes:
        vote_counter[i] += 1
        
    max_val = max(vote_counter)

    answer = []
    for idx in range(1, N + 1):
        if vote_counter[idx] == max_val:
            answer.append(vote_counter[idx])
    return answer


#The following is code to output testcase. The code below is correct and you shall correct solution function.
N1 = 5
votes1 = [1,5,4,3,2,5,2,5,5,4]
ret1 = solution(N1, votes1)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret1, " .")


N2 = 4
votes2 = [1, 3, 2, 3, 2]
ret2 = solution(N2, votes2)

#Press Run button to receive output.
print("Solution: return value of the function is ", ret2, " .")