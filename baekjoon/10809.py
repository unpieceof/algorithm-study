# 10809. 알파벳 찾기
word = list(input())
answer = ['-1']*26

for i in range(len(word)):
	chk = ord(word[i]) - 97
	if answer[chk] == '-1':
		answer[chk] = str(i)

print(' '.join(answer))