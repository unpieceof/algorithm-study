# 1152.단어의 개수
# '' <- 이것도 1개로 인식함
tmp_str = input()
trim_str = tmp_str.strip()
if trim_str == '':
    print(0)
else:
    print(len(trim_str.split(' ')))
