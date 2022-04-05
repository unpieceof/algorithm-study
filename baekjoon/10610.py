# 10610. 30
# sort, reverse의 Type은 None임 -> list return이 아니라 just operate?
# 가지치기 가능한 부분 확인 필요
num = input()
list_num = list(num)
sum_num = 0
z_flag = False

for i in list_num:
    sum_num += int(i)
    if i == '0':
        z_flag = True

if sum_num%3 == 0 and z_flag == True:
    list_num.sort(revrese=True)
    print(''.join(list_num))
else:
    print(-1)
