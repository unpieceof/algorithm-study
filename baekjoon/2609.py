# 2609. 최대공약수와 최소공배수
import math

def lcm(a, b):
    return (a * b) // math.gcd(a, b)

a, b = map(int, input().split())
print(math.gcd(a, b))
print(lcm(a, b)) # math.lcm 함수는 python 3.9 이상이어야 사용 가능
