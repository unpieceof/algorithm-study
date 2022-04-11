# 3052.나머지
answer = dict()
for _ in range(10):
    num = int(input())
    answer[num%42] = True

print(len(answer.keys()))
