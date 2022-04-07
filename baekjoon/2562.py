# 2562. 최댓값 
answer, cnt = 0, 0
for i in range(9):
	num = int(input())
	if num > answer:
		answer = num
		cnt = i+1
print(answer)
print(cnt)