# 1157. 단어 공부
word = list(input().lower())
word.sort()
answer = dict()

for c in word:
    try:
        answer[c] += 1
    except:
        answer[c] = 1

sort_ans = dict(sorted(answer.items(), key=lambda item: item[1], reverse=True))
list_ans = list(sort_ans.values())

if len(list_ans) == 1:
    print(word[0].upper())
elif list_ans[0] == list_ans[1]:
    print("?")
else:
    print(max(answer, key=answer.get).upper()) # 최대 value의 key 출력
