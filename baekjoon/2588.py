# 2588.곱셈
a = input()
b = input()
list_b = list(map(int, b))

answer = [0]*4
answer[0] = int(a)*list_b[2]
answer[1] = int(a)*list_b[1]
answer[2] = int(a)*list_b[0]
answer[3] = answer[0] + answer[1]*10 + answer[2]*100

for i in answer:
    print(i)
