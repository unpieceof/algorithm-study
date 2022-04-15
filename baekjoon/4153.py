# 4153. 직각삼각형
while(1):
	tri_num = list(map(int, input().split()))
	if sum(tri_num) == 0:
		exit()
	else:
		tri_num.sort()
		if tri_num[2]**2 == tri_num[0]**2 + tri_num[1]**2:
			print("right")
		else:
			print("wrong")