## lev: 몇 번째 카드를 뽑는 것인가?
## max_lev: 총 뽑을 카드의 수
number_list = []
def card_pick(lev, max_lev, card_cnt, card_used, number):
    if lev == max_lev:
        number_list.append(number)
        return
    
    for i in range(1, 10):
        if card_cnt[i] > card_used[i]:
            card_used[i] += 1
            card_pick(lev + 1, max_lev, card_cnt, card_used, number * 10 + i)
            card_used[i] -= 1

def solution(card, n):
    # 여기에 코드를 작성해주세요.
    card_cnt = [0] * 10
    card_used = [0] * 10
    for i in range(len(card)): card_cnt[card[i]] += 1

    card_pick(0, len(card), card_cnt, card_used, 0)

    answer = number_list.index(n) + 1 if n in number_list else -1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
card1 = [1, 1, 2, 3]
n1 = 3211
ret1 = solution(card1, n1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")