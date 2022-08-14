import sys

## 입력
input = sys.stdin.readline

N, K = map(int, input().split())

## 모든 바구니에 공을 하나씩 담는다
basket = [1] * K

N -= K

