# 1259. 팰린드롬수
while 1:
    num = input()
    list_num = list(num)
    
    if num == '0': exit()
    if len(num) == 1:
        print("yes")
        continue
    
    n = len(num)//2
    
    if len(num)%2 == 0:
        check_num = list_num[n:]
        check_num.reverse()
        if list_num[:n] == check_num:
            print("yes")
        else:
            print("no")
    else:
        check_num = list_num[n+1:]
        check_num.reverse()
        if list_num[:n] == check_num:
            print("yes")
        else:
            print("no")
