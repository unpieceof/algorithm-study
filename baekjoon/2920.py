# 2920. 음계
list_code = input().split()
if ''.join(list_code) == '12345678':
	print("ascending")
elif ''.join(list_code) == '87654321':
	print("descending")
else:
	print("mixed")