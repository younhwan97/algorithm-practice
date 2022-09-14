def solution(n, mix, k):
    answer = 0
    card = [_ for _ in range(1, n+1)]
    while mix != 0:
        mix = mix - 1
        card_a, card_b = [0 for _ in range(n//2)], [0 for _ in range(n//2)]
        for i in range(0, n):
            if i < n//2:
                card_a[i] = card[i]
            else:
                card_b[i] = card[i]
        for i in range(0, n):
            if i % 2 == 0:
                card[i] = card_a[i//2]
            else:
                card[i] = card_b[i//2]
    answer = card[k-1]
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
n = 6
mix = 3
k = 3
ret = solution(n, mix, k)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")