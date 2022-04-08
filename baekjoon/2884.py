# 2884. 알람 시계
hour, minute = map(int, input().split())
minute -= 45

if minute >= 0:
	print(hour, minute)
else:
	hour -= 1
	minute +=60
	if hour == -1:
		hour = 23
	print(hour, minute)