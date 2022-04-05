# 1546. 평균
num = int(input())
score = list(map(int, input().split()))

score.sort()
print((sum(score)/score[-1])*100/num)
