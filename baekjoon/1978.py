# 1978. 소수 찾기
# 에라토스테네스의 체 
from itertools import combinations
import sys
# list comprehension
p_num = [0, 0] + [i for i in range(2, 1001)] # 여길 1000으로 둬서 계속 IndexError 떴음

for i in range(len(p_num)):
    if p_num[i] != 0:
        for num in range(i * 2, len(p_num), i):
            p_num[num] = 0

answer = 0
num = int(input())
prime_list = map(int, sys.stdin.readline().strip().split())

for prime in prime_list:
    if p_num[prime] != 0:
        answer+=1

print(answer)
