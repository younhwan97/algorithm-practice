import sys
input = sys.stdin.readline


def change(target, changed, b_index):
    # 종료 조건
    if changed == b_index:
        return

    
    

                    
target = input().strip()
changed = set()
b_index = set()

for i in range(len(target)):
    if target[i] == 'b':
        b_index.add(i)

change(target, changed, b_index)