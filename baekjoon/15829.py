# 15829. Hashing
num = int(input())
word = list(input())
answer = [0]*num
for i in range(num):
	answer[i] = (ord(word[i]) - 96)*(31**i)

print(sum(answer)%1234567891)