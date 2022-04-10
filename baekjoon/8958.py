# 8958. OX퀴즈
num = int(input())
for _ in range(num):
	score, total = 0, 0
	test_case = list(input())
	for chk in test_case:
		if chk == 'O':
			score += 1
			total += score
		else:
			score = 0
	print(total)