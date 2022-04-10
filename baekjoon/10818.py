# 10818. 최소, 최대
cnt = int(input())
list_num = list(map(int, input().split()))
minn, maxn = list_num[0], list_num[0]

for num in list_num:
	if num < minn:
		minn = num
	elif num > maxn:
		maxn = num
		
print(minn, maxn)