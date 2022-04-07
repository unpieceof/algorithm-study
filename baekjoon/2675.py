# 2675. 문자열 반복
word_num = int(input())
answers = ['']*word_num

for i in range(word_num):
	re_cnt, word = input().split()
	list_word = list(word)
	for c in list_word:
		answers[i] += c*int(re_cnt)

for answer in answers:
	print(answer)
