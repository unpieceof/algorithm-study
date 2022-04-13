# 1181. 단어 정렬
num = int(input())
words = dict()

for _ in range(num):
	word = input()
	words[word] = len(word)

# 다중 조건으로 정렬할 경우, 튜플로 순서 지정
sorted_words = sorted(words.items(), key = lambda word: (word[1], word[0]))

for key, value in sorted_words:
	print(key)