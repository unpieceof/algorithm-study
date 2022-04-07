# 10951. A+B - 4
while(1):
	try:
		a, b = map(int, input().split())
		print(a+b)
	except: # 입력값 들어오지 않는 경우 에러 처리
		exit() # function이 아닌 경우 return으로 종료시킬 수 없다.