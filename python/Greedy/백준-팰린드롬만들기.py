name = list(input())

## 사전순으로 정렬
name.sort()

matched_index = [False] * (len(name))

answer= ""
pre = ""
mid = ""
post= ""

for i in range(0, len(name)):
    word = name[i]
    if i + 1 < len(name) and matched_index[i] == False and word == name[i + 1]:
        matched_index[i] = True
        matched_index[i + 1] = True
        pre += word
        post += word

unmatched_cnt = 0
for i in range(0, len(matched_index)):
    if matched_index[i] == False:
        unmatched_cnt += 1
        mid += name[i]

answer = pre + mid + post[::-1]

if unmatched_cnt > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer)