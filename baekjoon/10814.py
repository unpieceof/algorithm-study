# 10814. 나이순 정렬
num = int(input())
members = []
for _ in range(num):
    members.append(list(input().split()))

members.sort(key=lambda x:int(x[0]))
for member in members:
    print(member[0], member[1]) 
