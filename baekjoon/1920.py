# 1920. 수 찾기
target = int(input())
compare_list = list(map(int, input().split()))
compare_dict = {num:1 for num in compare_list} # True가 아니라 true로 쓰면 bool 값으로 인식하지 않

test_num = int(input())
test_list = list(map(int, input().split()))
for num in test_list:
	try:
		print(compare_dict[num])
	except:
		print(0)