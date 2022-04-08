# 10952. A+B -5
while(1):
	try:
		a, b = map(int, input().split())
		if a + b == 0:
			exit()
		else:
			print(a + b)
	except:
		exit()