# 11050. 이항 계수 1
def factorial(num):
	result = 1
	for i in range(num):
		result*=(num - i)
	return result

n, k = map(int, input().split())
print(int(factorial(n)/(factorial(k)*factorial(n-k))))