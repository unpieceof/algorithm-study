# 11720. 숫자의 합
num = int(input()) # 이 input은 필요 없는 듯
str_num = input()
list_num = map(int, list(str_num))

answer = 0
for n in list_num:
	answer += n

print(answer)