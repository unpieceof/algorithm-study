# 10950. A+B -3
cnt = int(input())
answer = [0]*cnt

for i in range(cnt):
	a, b = map(int, input().split())
	answer[i] = a + b

for ans in answer:
	print(ans)
		